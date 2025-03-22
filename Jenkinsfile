pipeline {
    agent any

    parameters {
        string(name: 'AWS_REGION', defaultValue: 'us-east-1', description: 'AWS Region')
        string(name: 'AWS_ACCOUNT_ID', defaultValue: '652926606685', description: 'AWS Account ID')
        string(name: 'EC2_INSTANCE_ID', defaultValue: 'i-0c8eaf55415f15da9', description: 'EC2 Instance ID')
    }

    environment {
        ECR_REPO = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/power-meter-selector"
        IMAGE_TAG = "${new java.text.SimpleDateFormat('yyyyMMdd').format(new Date())}-${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout Code') {
            steps {
                cleanWs()
                checkout scm
            }
        }

        stage('Build, Tag & Push Docker Image') {
            steps {
                script {
                    try {
                        withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: '502817983', accessKeyVariable: 'AWS_ACCESS_KEY_ID', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
                            sh """
                            export DOCKER_BUILDKIT=1
                            docker run --rm -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY amazon/aws-cli ecr get-login-password --region ${env.AWS_REGION} | docker login --username AWS --password-stdin ${ECR_REPO}
                            docker build -t power-meter-selector:${IMAGE_TAG} .
                            docker tag power-meter-selector:${IMAGE_TAG} ${ECR_REPO}:${IMAGE_TAG}
                            docker push ${ECR_REPO}:${IMAGE_TAG}
                            """
                        }
                    } catch (Exception e) {
                        error "Docker build/push failed: ${e.message}"
                    }
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                script {
                    try {
                        withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: '502817983', accessKeyVariable: 'AWS_ACCESS_KEY_ID', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
                            def imageDigest = sh(script: "docker inspect ${ECR_REPO}:${IMAGE_TAG} --format '{{.Id}}'", returnStdout: true).trim()
                            echo "Built image digest: ${imageDigest}"

                            // Define the commands as a properly escaped string
                            def commands = [
                                "docker run --rm -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY amazon/aws-cli ecr get-login-password --region ${env.AWS_REGION} | docker login --username AWS --password-stdin ${ECR_REPO}",
                                "docker rmi ${ECR_REPO}:${IMAGE_TAG} || true",
                                "docker pull ${ECR_REPO}:${IMAGE_TAG}",
                                "docker stop power-meter-selector || true",
                                "docker rm power-meter-selector || true",
                                "nohup docker run -d --name power-meter-selector -p 8000:8080 ${ECR_REPO}:${IMAGE_TAG} &",
                                "sleep 5",
                                "docker inspect power-meter-selector --format '{{.Image}}' > /tmp/deployed_image.txt"
                            ].join('","')

                            // First SSM command to deploy the container
                            def commandId = sh(script: """
                                docker run --rm -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY \
                                amazon/aws-cli ssm send-command \
                                --document-name "AWS-RunShellScript" \
                                --targets '[{"Key":"InstanceIds","Values":["${EC2_INSTANCE_ID}"]}]' \
                                --parameters '{\"commands\": [\"${commands}\"]}' \
                                --region ${env.AWS_REGION} \
                                --timeout-seconds 300 \
                                --output text | grep -o '[a-f0-9]\\{8\\}-[a-f0-9]\\{4\\}-[a-f0-9]\\{4\\}-[a-f0-9]\\{4\\}-[a-f0-9]\\{12\\}' | head -n 1
                            """, returnStdout: true).trim()
                            echo "Command ID: ${commandId}"

                            // Wait for the command to complete and retry if necessary
                            def maxRetries = 3
                            def retryCount = 0
                            def deployedDigest = ""

                            while (retryCount < maxRetries) {
                                try {
                                    sleep 10 // Wait for the command to complete
                                    deployedDigest = sh(script: """
                                        docker run --rm -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY \
                                        amazon/aws-cli ssm get-command-invocation \
                                        --command-id ${commandId} \
                                        --instance-id ${EC2_INSTANCE_ID} \
                                        --region ${env.AWS_REGION} \
                                        --query 'StandardOutputContent' \
                                        --output text | grep -o 'sha256:[a-f0-9]*' | head -n 1
                                    """, returnStdout: true).trim()
                                    echo "Deployed image digest: ${deployedDigest}"
                                    break
                                } catch (Exception e) {
                                    retryCount++
                                    echo "Failed to retrieve command invocation (attempt ${retryCount}/${maxRetries}): ${e.message}"
                                    if (retryCount == maxRetries) {
                                        error "Failed to retrieve deployed digest after ${maxRetries} attempts: ${e.message}"
                                    }
                                    sleep 10
                                }
                            }

                            if (deployedDigest && deployedDigest != imageDigest) {
                                error "Deployed image digest (${deployedDigest}) does not match built image digest (${imageDigest})"
                            }
                            echo "Verified: Deployed image matches built image"
                        }
                    } catch (Exception e) {
                        error "Deployment failed: ${e.message}"
                    }
                }
            }
        }
    }

    post {
        success {
            echo "Deployed version ${IMAGE_TAG} successfully!"
        }
        failure {
            echo "Pipeline failed. Check logs for details."
        }
    }
}