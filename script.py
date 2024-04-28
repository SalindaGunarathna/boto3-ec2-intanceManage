import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Get list of instances
instances = ec2.describe_instances()

for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        state = instance['State']['Name']
        print("Instance ID:", instance_id)
        print("State:", state)
        if state == 'running':
            print("Stopping instance...")
            ec2.stop_instances(InstanceIds=[instance_id])
            print("Instance stopped")
        print()
