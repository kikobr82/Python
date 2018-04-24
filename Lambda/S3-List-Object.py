#!/usr/bin/env python
import boto3
import sys
bucket_list = sys.argv[1]
print 'Bucket that will be listed:', bucket_list

client = boto3.client('s3')

response = client.list_objects_v2(Bucket = str(bucket_list))

for obj in response['Contents']:
    print 'Object Name: %s' % obj['Key']
