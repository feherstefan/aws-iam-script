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
