
import linode_api4

# Replace with your Linode API token
API_TOKEN = 'd25075c16187148666fb92e88b8d3e1c3c5c60c664bc518cc6369a5dbd1a78c3'

# Create a Linode API client
client = linode_api4.LinodeClient(API_TOKEN)

print(client.regions)
'''
# Get a list of all Linode instances
instances = client.get(linode_api4.Instance)

# Print the details of each instance
for instance in instances:
    print(f"Instance ID: {instance.id}")
    print(f"Label: {instance.label}")
    print(f"Region: {instance.region}")
    print(f"Type: {instance.type}")
    print(f"Status: {instance.status}")
    print(f"IP Address: {instance.ip_addresses.public.ipv4}")
    print(f"CPU: {instance.cpu}")
    print(f"RAM: {instance.ram} MB")
    print(f"Disk: {instance.disk} GB")
    print(f"Backups: {'Enabled' if instance.backups.enabled else 'Disabled'}")
    print("---")




'''