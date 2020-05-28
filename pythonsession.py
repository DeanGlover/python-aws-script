# coding: utf-8
get_ipython().run_line_magic('history', '')
import boto3
session = boto3.Session(profile_name='default')
s3 = session.resource('s3')
for bucket in s3.buckets.all():
    print(bucket)
    
new_bucket = s3.create_bucket(Bucket='deanglover354654', CreateBucketConfiguration={'LocationConstraint' : 'ap-southeast-2'})
get_ipython().run_line_magic('history', '')
get_ipython().run_line_magic('save', 'pythonsession.py 1-10')
