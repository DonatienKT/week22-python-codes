import boto3

_ec2 = boto3.client('ec2',region_name='us-east-1')
response = _ec2.describe_instances()


'''inst_list=[]
for int in response['Reservations']:
    #print("*******************************")
    inst_list.append(int['Instances'][0]['InstanceId'])

print(inst_list)'''

instan=[]
for res in response['Reservations']:
    print("*******************************")
    instan.append(res)

print(instan)

