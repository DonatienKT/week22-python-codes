import boto3

_ec2 = boto3.client('ec2', region_name="us-east-1")
#_iam = boto3.client('iam')
#_s3 = boto3.client('ec2')

inst_state = 'stopped'

dev_filter = {'Name': 'tag:env', 'Values': ['dev']}
qa_filter = {'Name': 'tag:env', 'Values': ['qa']}
prod_filter = {'Name': 'tag:env', 'Values': ['dev']} 
inst_typ_filter = {'Name': 'instance-type', 'Values': ['t2.micro']}
#stopped_inst = {'Name': 'instance-state-name', 'Values': ['stopped']}
inst_stat = {'Name': 'instance-state-name', 'Values': [inst_state]}


def listInstances(args):

    try:
        response = _ec2.describe_instances(Filters=[args])
        instance_list = []
        for instance in response['Reservations']:
            inst_ids = instance['Instances'][0]['InstanceId']
            instance_list.append(inst_ids)
            
        return instance_list
    except Exception as e:
        print(f"ERROR: {e}")


def startInstances(instance_list):
    try: 
        _ec2.start_instances(InstanceIds=instance_list)
    except Exception as e:
        print(f"ERROR: {e}")

def main():
    s = listInstances()
    startInstances(s)

print("Instances started successfully!")

if __name__ == "__main__":
    main()    