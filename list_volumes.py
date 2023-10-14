import boto3

if __name__ == '__main__':
    session = boto3.Session(profile_name='default')
    ec2_client = session.client('ec2',
                                region_name='us-east-1')
#     response = ec2_client.describe_volumes()
#     print("Response : " + str(response))
#     print("Volumes: " + str(response["Volumes"]))
#     print("Volume[0] " + str(response["Volumes"][0]))
#     print("Volumes[0][Attachments] : " + str(response["Volumes"][0]["Attachments"][0]))
#     #Print("End Gaul : ")




    # ec2_client = session.client('ec2',
    #                           region_name='us-east-1')
    response = ec2_client.describe_volumes()
    print("Response : " + str(response))
    # print("Volumes : " + str(response["Volumes"]))
    # print("Volumes[0] : " + str(response["Volumes"][0]))
    # print("Volumes[0][Attachments] : " + str(response["Volumes"][0]["Attachments"]))
    # print("Attachments [0] : " + str(response["Volumes"][0]["Attachments"][0]))
    # print("End Goal : " + str(response["Volumes"][0]["Attachments"][0]["VolumeId"]))
    # print(response['Volumes'][0]["Attachments"][0]['VolumeId'])
    for volume in response['Volumes']:
        print("volume id : " + str(volume["VolumeId"]))

#
#
#
# import boto3
#
# if __name__ == '__main__':
#     ec2_client = boto3.client('ec2',
#                               profile_name='default'
#                               )
#     response = ec2_client.describe_instances()
#     print(response)
#
#



