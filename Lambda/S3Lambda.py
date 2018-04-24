import boto3
def lambda_handler(event, context):
    client = boto3.client('s3')
    try:
        response = client.list_objects_v2(Bucket = event['chosen_bucket'])

        dict = {}
        index = 0
        for obj in response['Contents']:
            index = index + 1
            dict[index] = obj['Key']

        return {
            'objects' :  dict
        }
    except Exception as error:
        return {
            'message' : 'Bucket informed not valid'
        }