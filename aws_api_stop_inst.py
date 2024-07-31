import boto3 

_ec2 = boto3.client('ec2',region_name='us-east-1')
response = _ec2.describe_instances()

inst_list=[]
for int in response['Reservations']:
    #print("*******************************")
    inst_list.append(int['Instances'][0]['InstanceId'])

print(inst_list)

try:
    _ec2.stop_instances(InstanceIds=inst_list)
except Exception as e:
    print(f"Error: {e}")