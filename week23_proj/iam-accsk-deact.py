import boto3, datetime
from datetime import date
from botocore.exceptions import ClientError
import email

AWS_REGION= "us-east-1"

email_list = ['donatienken@yahoo.com']

iam = boto3.client('iam', region_name=AWS_REGION)

def send_mail(email_list):
    # emails in email_list must be verified by AWS SES
    RECIPIENTS = email_list
    # set your verified email address from AWS SES
    SENDER = "donaskt@gmail.com"
    SUBJECT = "WARNING!!! IAM Access Key Rotation"
    BODY_TEXT = ("Your IAM Access Key need to be rotated immediately as it is 3 months or older.\n" 
                "If not, it will be deactivated shortly.")           
    CHARSET = "UTF-8"
    ses_client = boto3.client('ses', region_name=AWS_REGION)
    # verify if the configuration set is created, if not then create it
    try:
        response = ses_client.create_configuration_set(
            ConfigurationSet={
                'Name': 'my-config-set'
            }
        )   
    except Exception as e:
        print('Configuration set exists:' + e.response['Error']['Message'])
    else:
        print(f'Configuration set creation error !!! Please check your configuration set')
    # send email
    try:
        response = ses_client.send_email(
            Destination={
                'ToAddresses': RECIPIENTS,
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
            ConfigurationSetName='my-config-set',
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print(f"Email sent! Message ID: {response['MessageId']}")

for user in iam.list_users()['Users']: # check for all iam users 
    # get a list of access keys for a user
    userKeys = iam.list_access_keys(UserName=user['UserName'])
    for keyValue in userKeys['AccessKeyMetadata']:
        # check if access key is active
        if keyValue['Status'] == 'Active':
            currentdate = date.today()
            active_days = currentdate - keyValue['CreateDate'].date()
            userTags = iam.list_user_tags(UserName=user['UserName'])
            if (active_days >= datetime.timedelta(days=90)):
                # get the list of email from tags as key:value
                email_tags = list(filter(lambda tag: tag['Key'] == 'email', userTags['Tags']))
                # make a list of email from tags 
                for email_tag in email_tags:
                    email = email_tag['Value']
                    email_list.append(email)
                    print(email)
                print(f"Access key: {keyValue[ 'AccessKeyId']} of {keyValue['UserName']} need to be rotated")
                # deactivate keys 
                #iam.update_access_key(UserName=keyValue['UserName'], AccessKeyId=keyValue['AccessKeyId'], Status='Inactive')
            else:
                print(f"Access key: {keyValue[ 'AccessKeyId']} of {keyValue['UserName']} have been rotated")
        else:
            print(f"The Access key : {keyValue[ 'AccessKeyId']}  of {user} is inactive !!!")

# to remove duplicated emails
email_unique = list(set(email_list))
if len(email_unique) >= 1:
    send_mail(email)
else:
    print('There is no email address in the tags or all access keys have been rotated')