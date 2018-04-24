#!/usr/bin/env python
import boto3
import sys
s3 = boto3.resource('s3')
dict = {}
index = 0
print 'Existent buckets:'
for bucket in s3.buckets.all():
    index = index + 1
    dict[index] = str(bucket.name) 
    print('Bucket {0} is {1} '.format(index, bucket.name))

chosen_bucket = input('Select the number of the bucket to be listed: ')

if chosen_bucket > index:
    print 'This bucket does not exists'
else:
    client = boto3.client('s3')
    response = client.list_objects_v2(Bucket = str(dict[chosen_bucket]))
    for obj in response['Contents']:
        print 'Object Name: %s' % obj['Key']
