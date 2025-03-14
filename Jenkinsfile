pipeline {
    agent any

    parameters {
        string(name: 'AWS_REGION', defaultValue: 'us-east-1', description: 'AWS Region')
        string(name: 'AWS_ACCOUNT_ID', defaultValue: '652926606685', description: 'AWS Account ID')
        string(name: 'EC2_INSTANCE_ID', defaultValue: 'i-0c8eaf55415f15da9', description: 'EC2 Instance ID')
    }

    environment {
        ECR_REPO = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/power-meter"
        AWS_CREDENTIALS = credentials('502817983')
        IMAGE_TAG = "${new java.text.SimpleDateFormat('yyyyMMdd').format(new Date())}-${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Create ECR Repository') {
            steps {
                script {
                    try {
                        withAWS(credentials: '502817983', region: "${AWS_REGION}") {
                            sh """
                            aws ecr describe-repositories --repository-names power-meter --region ${env.AWS_REGION} || \
                            aws ecr create-repository --repository-name power-meter --region ${env.AWS_REGION}
                            """
                        }
                    } catch (Exception e) {
                        echo "ECR repository creation/verification failed, but proceeding: ${e.message}"
                    }
                }
            }
        }

        stage('Build, Tag & Push Docker Image') {
            steps {
                script {
                    try {
                        withAWS(credentials: '502817983', region: "${AWS_REGION}") {
                            sh """
                            aws ecr get-login-password --region ${env.AWS_REGION} | docker login --username AWS --password-stdin ${ECR_REPO}
                            docker build -t power-meter:${IMAGE_TAG} .
                            docker tag power-meter:${IMAGE_TAG} ${ECR_REPO}:${IMAGE_TAG}
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
                        withAWS(credentials: '502817983', region: "${AWS_REGION}") {
                            def imageDigest = sh(script: "docker inspect ${ECR_REPO}:${IMAGE_TAG} --format '{{.Id}}'", returnStdout: true).trim()
                            echo "Built image digest: ${imageDigest}"

                            sh """
                            aws ssm send-command \
                                --document-name "AWS-RunShellScript" \
                                --targets '[{"Key":"InstanceIds","Values":["${EC2_INSTANCE_ID}"]}]' \
                                --parameters '{
                                    "commands": [
                                        "aws ecr get-login-password --region ${env.AWS_REGION} | docker login --username AWS --password-stdin ${ECR_REPO}",
                                        "docker rmi ${ECR_REPO}:${IMAGE_TAG} || true",
                                        "docker pull ${ECR_REPO}:${IMAGE_TAG}",
                                        "docker stop my-container || true",
                                        "docker rm my-container || true",
                                        "nohup docker run -d --name my-container -p 8000:8000 ${ECR_REPO}:${IMAGE_TAG} &",
                                        "sleep 5",
                                        "docker inspect my-container --format '{{.Image}}' > /tmp/deployed_image.txt"
                                    ]
                                }' \
                                --region ${env.AWS_REGION} \
                                --timeout-seconds 300 \
                                --output text
                            """

                            def deployedDigest = sh(script: """
                                aws ssm send-command \
                                    --document-name "AWS-RunShellScript" \
                                    --targets '[{"Key":"InstanceIds","Values":["${EC2_INSTANCE_ID}"]}]' \
                                    --parameters 'commands=["cat /tmp/deployed_image.txt"]' \
                                    --region ${env.AWS_REGION} \
                                    --output text | tail -n 1
                                """, returnStdout: true).trim()
                            
                            if (deployedDigest != imageDigest) {
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
        always {
            cleanWs()
        }
        success {
            echo "Deployed version ${IMAGE_TAG} successfully!"
        }
        failure {
            echo "Pipeline failed. Check logs for details."
        }
    }
}