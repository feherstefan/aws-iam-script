# README

## AWS IAM User Creation Script

This script creates three users in AWS Identity and Access Management (IAM) with different permissions:
- `AdminUser` with full administrative rights
- `S3AdminUser` with permissions to administer S3 buckets
- `EC2AdminUser` with permissions to administer EC2 instances

## Prerequisites

1. **AWS Account**: You need an AWS account to create IAM users and assign permissions.
2. **AWS CLI**: The AWS Command Line Interface (CLI) must be installed and configured on your machine.
3. **Python**: Python should be installed on your machine.
4. **boto3**: The AWS SDK for Python, `boto3`, should be installed.

## Step-by-Step Guide

### 1. Install AWS CLI

If you haven't installed the AWS CLI, follow these steps:

- **Windows**:
  Download and run the installer from the AWS CLI official website: [AWS CLI Installer for Windows](https://aws.amazon.com/cli/).

- **macOS**:
  Use Homebrew to install the AWS CLI:
  ```sh
  brew install awscli
  ```

- **Linux**:
  Use the package manager to install the AWS CLI. For example, on Ubuntu:
  ```sh
  sudo apt-get update
  sudo apt-get install awscli
  ```

Verify the installation:
```sh
aws --version
```

### 2. Configure AWS CLI

Configure the AWS CLI with your credentials and default region:
```sh
aws configure
```
You will be prompted to enter:
- AWS Access Key ID
- AWS Secret Access Key
- Default region name (e.g., `us-west-2`)
- Default output format (e.g., `json`)

### 3. Install Python

Download and install Python from the official website: [Python Downloads](https://www.python.org/downloads/).

Verify the installation:
```sh
python --version
```

### 4. Install boto3

Install `boto3` using pip:
```sh
pip install boto3
```

### 5. Create the Script

Create a Python script file, e.g., `create_iam_users.py`, and paste the following code into it:

```python
import boto3
import json

# Initialize a session using the default profile
session = boto3.Session(profile_name='default')
iam = session.client('iam')

# User definitions
users = [
    {
        'UserName': 'AdminUser',
        'PolicyName': 'AdminPolicy',
        'PolicyDocument': {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": "*",
                    "Resource": "*"
                }
            ]
        }
    },
    {
        'UserName': 'S3AdminUser',
        'PolicyName': 'S3AdminPolicy',
        'PolicyDocument': {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": [
                        "s3:*"
                    ],
                    "Resource": "*"
                }
            ]
        }
    },
    {
        'UserName': 'EC2AdminUser',
        'PolicyName': 'EC2AdminPolicy',
        'PolicyDocument': {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": [
                        "ec2:*"
                    ],
                    "Resource": "*"
                }
            ]
        }
    }
]

# Create users and attach policies
for user in users:
    try:
        # Create user
        response = iam.create_user(UserName=user['UserName'])
        print(f"Created user {user['UserName']}")

        # Create the inline policy
        policy_response = iam.put_user_policy(
            UserName=user['UserName'],
            PolicyName=user['PolicyName'],
            PolicyDocument=json.dumps(user['PolicyDocument'])
        )
        print(f"Attached policy {user['PolicyName']} to user {user['UserName']}")

    except Exception as e:
        print(f"Error creating user {user['UserName']}: {e}")

print("Script completed.")
```

### 6. Run the Script

Run the script using Python:
```sh
python create_iam_users.py
```
The script will create three users (`AdminUser`, `S3AdminUser`, `EC2AdminUser`) and attach the respective policies to them.

### 7. Verify the Users and Policies

To verify that the users and policies have been created correctly, use the AWS CLI commands:

- **List Users**:
  ```sh
  aws iam list-users
  ```

- **List User Policies**:
  ```sh
  aws iam list-user-policies --user-name AdminUser
  aws iam list-user-policies --user-name S3AdminUser
  aws iam list-user-policies --user-name EC2AdminUser
  ```

- **Get Policy Document**:
  ```sh
  aws iam get-user-policy --user-name AdminUser --policy-name AdminPolicy
  aws iam get-user-policy --user-name S3AdminUser --policy-name S3AdminPolicy
  aws iam get-user-policy --user-name EC2AdminUser --policy-name EC2AdminPolicy
  ```

### Example Commands and Expected Output

1. **List Users**:

```sh
aws iam list-users
```

Expected output should include the users you created:

```json
{
    "Users": [
        {
            "UserName": "AdminUser",
            "UserId": "AIDAEXAMPLE1",
            "Arn": "arn:aws:iam::123456789012:user/AdminUser",
            ...
        },
        {
            "UserName": "S3AdminUser",
            "UserId": "AIDAEXAMPLE2",
            "Arn": "arn:aws:iam::123456789012:user/S3AdminUser",
            ...
        },
        {
            "UserName": "EC2AdminUser",
            "UserId": "AIDAEXAMPLE3",
            "Arn": "arn:aws:iam::123456789012:user/EC2AdminUser",
            ...
        }
    ]
}
```

2. **List User Policies**:

```sh
aws iam list-user-policies --user-name AdminUser
```

Expected output:

```json
{
    "PolicyNames": [
        "AdminPolicy"
    ]
}
```

3. **Get Policy Document**:

```sh
aws iam get-user-policy --user-name AdminUser --policy-name AdminPolicy
```

Expected output:

```json
{
    "UserName": "AdminUser",
    "PolicyName": "AdminPolicy",
    "PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "*",
                "Resource": "*"
            }
        ]
    }
}
```

Repeat the commands for `S3AdminUser` and `EC2AdminUser` with their respective policy names.

## Conclusion

By following the above steps, you can create IAM users with specific permissions using the AWS CLI and a Python script. This ensures that each user has the correct level of access as defined in the policies.