import boto3


def list_volumes(ec2_client):
    response = ec2_client.describe_volumes()
    # print("Response : " + str(response))

    for volume in response['Volumes']:
        # print("volume id : " + str(volume["VolumeId"]) + " State : "+ str(volume["State"]))
        if volume["State"] != 'in-use':
            print("Categorizing volume to be deleted: " + str(volume["VolumeId"]) + " State : " + str(volume["State"]))
            del_volume(ec2_client,volume["VolumeId"])


def del_volume(ec2_client, volume_id):
    response = ec2_client.delete_volume(
        VolumeId=volume_id
    )
    print("Volume : "+str(volume_id)+" has been deleted")


def lambda_handler(event, context):
    ec2_client = boto3.client("ec2", region_name='ap-south-1')
    list_volumes(ec2_client)

if __name__ == '__main__':
    session = boto3.Session(profile_name='myprofile')
    ec2_client = session.client('ec2',
                                region_name='ap-south-1')
    list_volumes(ec2_client)
