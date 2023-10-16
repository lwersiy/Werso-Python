
########### FOR KEY AGE IN SECONDS, USE THIS CODE ###########
import boto3
from datetime import datetime, timezone

# Define the maximum age for access keys in hours (1 hour)
KEY_MAXIMUM_AGE_HOURS = 1

# Modify the key_age function to calculate age in hours
def key_age(access_key_creation_date):
    current_date = datetime.now(timezone.utc)
    age = current_date - access_key_creation_date
    return age.total_seconds() / 3600  # Convert age to hours

def lambda_handler(event, context):
    # Initialize the IAM client
    client = boto3.client('iam', region_name='us-east-1')
    # Initialize the SNS client
    sns_client = boto3.client('sns')

    # Define the IAM user to exclude from rotation
    EXCLUDED_USER = 'Admin-User'

    # Define the SNS topic ARN to which the notifications will be sent
    SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:989589514705:Key-rotator-notification'

    # List all IAM users
    iam_all_users = client.list_users()

    for user in iam_all_users['Users']:
        iam_user = user['UserName']

        # Skip the excluded user
        if iam_user == EXCLUDED_USER:
            print(f'Skipping access key rotation for user: {iam_user}')
            continue

        # List access keys for the current IAM user
        response = client.list_access_keys(UserName=iam_user)

        for access_key in response['AccessKeyMetadata']:
            access_key_id = access_key['AccessKeyId']
            access_key_creation_date = access_key['CreateDate']

            print(f'IAM UserName: {iam_user}, AccessKeyId: {access_key_id}, CreationDate: {access_key_creation_date}')

            # Calculate key age
            age = key_age(access_key_creation_date)

            # Check key age and deactivate if it exceeds the maximum age
            if age > KEY_MAXIMUM_AGE_HOURS:
                print(f'Deactivating the key for user {iam_user} as it exceeds the maximum key age')
                client.update_access_key(UserName=iam_user, AccessKeyId=access_key_id, Status='Inactive')

                # Add code to delete inactive access keys
                if access_key['Status'] == 'Inactive':
                    print(f'Deleting inactive key for user {iam_user}')
                    client.delete_access_key(UserName=iam_user, AccessKeyId=access_key_id)

                # Create a new access key
                response = client.create_access_key(UserName=iam_user)
                new_access_key = response['AccessKey']
                new_access_key_id = new_access_key['AccessKeyId']
                new_secret_access_key = new_access_key['SecretAccessKey']
                print('New AccessKeyId:', new_access_key_id)
                print('New SecretAccessKey:', new_secret_access_key)

                # Publish a message to the SNS topic for email notification
                message = f'Access key rotated for IAM user: {iam_user}\nNew Access Key ID: {new_access_key_id}'
                sns_client.publish(TopicArn=SNS_TOPIC_ARN, Message=message, Subject='Access Key Rotation')

    return {
        'statusCode': 200,
        'body': 'Lambda function executed successfully!'
    }

#




############## FOR KEY AGE IN DAYS, USE THIS CODE CODE ###############

# import boto3
# from datetime import datetime, timezone

# def key_age(access_key_creation_date):
#     current_date = datetime.now(timezone.utc)
#     age = current_date - access_key_creation_date
#     return age.days

# def lambda_handler(event, context):
#     # Initialize the IAM client
#     client = boto3.client('iam', region_name='us-east-1')
#     # Initialize the SNS client
#     sns_client = boto3.client('sns')

#     # Define the maximum age for access keys in days
#     KEY_MAXIMUM_AGE = 1

#     # Define the IAM user to exclude from rotation
#     EXCLUDED_USER = 'Admin-User'

#     # Define the SNS topic ARN to which the notifications will be sent
#     SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:989589514705:Key-rotator-notification'

#     # List all IAM users
#     iam_all_users = client.list_users()

#     for user in iam_all_users['Users']:
#         iam_user = user['UserName']

#         # Skip the excluded user
#         if iam_user == EXCLUDED_USER:
#             print(f'Skipping access key rotation for user: {iam_user}')
#             continue

#         # List access keys for the current IAM user
#         response = client.list_access_keys(UserName=iam_user)

#         for access_key in response['AccessKeyMetadata']:
#             access_key_id = access_key['AccessKeyId']
#             access_key_creation_date = access_key['CreateDate']

#             print(f'IAM UserName: {iam_user}, AccessKeyId: {access_key_id}, CreationDate: {access_key_creation_date}')

#             # Calculate key age
#             age = key_age(access_key_creation_date)

#             # Check key age and deactivate if it exceeds the maximum age
#             if age > KEY_MAXIMUM_AGE:
#                 print(f'Deactivating the key for user {iam_user} as it exceeds the maximum key age')
#                 client.update_access_key(UserName=iam_user, AccessKeyId=access_key_id, Status='Inactive')

#                  # Add code to delete inactive access keys
#                 if access_key['Status'] == 'Inactive':
#                     print(f'Deleting inactive key for user {iam_user}')
#                     client.delete_access_key(UserName=iam_user, AccessKeyId=access_key_id)

#                 # Create a new access key
#                 response = client.create_access_key(UserName=iam_user)
#                 new_access_key = response['AccessKey']
#                 new_access_key_id = new_access_key['AccessKeyId']
#                 new_secret_access_key = new_access_key['SecretAccessKey']
#                 print('New AccessKeyId:', new_access_key_id)
#                 print('New SecretAccessKey:', new_secret_access_key)

#                 # Publish a message to the SNS topic for email notification
#                 message = f'Access key rotated for IAM user: {iam_user}\nNew Access Key ID: {new_access_key_id}'
#                 sns_client.publish(TopicArn=SNS_TOPIC_ARN, Message=message, Subject='Access Key Rotation')

#     return {
#         'statusCode': 200,
#         'body': 'Lambda function executed successfully!'
#     }


#
#
# ####################### MY CODE #########################
#
# import boto3
# from datetime import datetime, timezone
#
# # Initialize the IAM client
# client = boto3.client('iam', region_name='us-east-1')
#
# # List current access keys for a specific user
# response = client.list_access_keys(UserName='python-user')
# print('Current access keys:', response)
#
#
# # Create a new access key
# response = client.create_access_key(UserName='python-user')
# access_key = response['AccessKey']
# access_key_id = access_key['AccessKeyId']
# secret_access_key = access_key['SecretAccessKey']
#
#
# # Print or use the access key details as needed
# print('New AccessKeyId:', access_key_id)
# print('New SecretAccessKey:', secret_access_key)
#
#
#
# # Print or use the access key details as needed
# print('New AccessKeyId:', access_key_id)
# print('New SecretAccessKey:', secret_access_key)
#
#
# # Define a function to calculate key age in days
# def key_age(access_key_creation_date, user_creation_date):
#     current_date = datetime.now(timezone.utc)
#     age = current_date - access_key_creation_date
#     return age.days
#
#
# # List all IAM users
# iam_all_users = client.list_users()
#
# # Define the maximum age for access keys in days
# KEY_MAXIMUM_AGE = 1
#
# for user in iam_all_users['Users']:
#     iam_user = user['UserName']
#
#     # List access keys for the current IAM user
#     response = client.list_access_keys(UserName=iam_user)
#
#     for access_key in response['AccessKeyMetadata']:
#         access_key_id = access_key['AccessKeyId']
#         access_key_creation_date = access_key['CreateDate']
#
#         print(f'IAM UserName: {iam_user}, AccessKeyId: {access_key_id}, CreationDate: {access_key_creation_date}')
#
#         # Calculate key age
#         age = key_age(access_key_creation_date, user_creation_date=access_key_creation_date)
#
#
# # List all IAM users
# iam_all_users = client.list_users()
#
# # Define the maximum age for access keys in days
# KEY_MAXIMUM_AGE = 1
#
# for user in iam_all_users['Users']:
#     iam_user = user['UserName']
#
#     # List access keys for the current IAM user
#     response = client.list_access_keys(UserName=iam_user)
#
#     for access_key in response['AccessKeyMetadata']:
#         access_key_id = access_key['AccessKeyId']
#         access_key_creation_date = access_key['CreateDate']
#
#         print(f'IAM UserName: {iam_user}, AccessKeyId: {access_key_id}, CreationDate: {access_key_creation_date}')
#
#         # Calculate key age
#         age = key_age(access_key_creation_date, user_creation_date=access_key_creation_date)
#
#
#         # Check key age and deactivate if it exceeds the maximum age
#         if age > KEY_MAXIMUM_AGE:
#             print(f'Deactivating the key for user {iam_user} as it exceeds the maximum key age')
#             client.update_access_key(UserName=iam_user, AccessKeyId=access_key_id, Status='Inactive')
#
#
# def lambda_handler(event, context, user_creation_date=2023-10-14):
#     # Initialize the IAM client
#     client = boto3.client('iam', region_name='us-east-1')
#     key_age(access_key_creation_date, user_creation_date)
#
#
#     # Rest of the code here...
#
#     return {
#         'statusCode': 200,
#         'body': 'Lambda function executed successfully!'
#     }
#
#
#
