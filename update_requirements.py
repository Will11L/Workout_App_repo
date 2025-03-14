import subprocess

# Run pip freeze and capture the output
result = subprocess.run(['pip', 'freeze'], capture_output=True, text=True)
requirements = result.stdout.splitlines()

# Define platform-specific requirements
platform_specifics = {
    'pywin32': "pywin32==308; sys_platform == 'Windows'",
    'pywinpty': "pywinpty==2.0.15; sys_platform == 'Windows'"
}

# Create a dictionary of regular requirements to easily update them
requirements_dict = {line.split('==')[0]: line for line in requirements if '==' in line}

# Update or add platform-specific requirements
for package, spec in platform_specifics.items():
    requirements_dict[package] = spec

# Convert the dictionary back to a list
updated_requirements = list(requirements_dict.values())

# Write to requirements.txt
with open('requirements.txt', 'w') as f:
    f.write('\n'.join(updated_requirements) + '\n')

print("requirements.txt has been updated with platform-specific conditions.")