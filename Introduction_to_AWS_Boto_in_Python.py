##############################
# Putting Files in the Cloud #
##############################

### Boto3 client

# Generate the boto3 client for interacting with S3
s3 = boto3.client('s3', region_name='us-east-1', 
                        # Set up AWS credentials 
                        aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)
# List the buckets
buckets = s3.list_buckets()

# Print the buckets
print(buckets)


### Multiple clients

# Generate the boto3 client for interacting with S3 and SNS
s3 = boto3.client('s3', region_name='us-east-1', 
                         aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)

sns = boto3.client('sns', region_name='us-east-1', 
                         aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)

# List S3 buckets and SNS topics
buckets = s3.list_buckets()
topics = sns.list_topics()

# Print out the list of SNS topics
print(topics)


### Creating a bucket

import boto3

# Create boto3 client to S3
s3 = boto3.client('s3', region_name='us-east-1', 
                         aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)

# Create the buckets
response_staging = s3.create_bucket(Bucket='gim-staging')
response_processed = s3.create_bucket(Bucket='gim-processed')
response_test = s3.create_bucket(Bucket='gim-test')

# Print out the response
print(response_staging)


### Listing buckets

# Get the list_buckets response
response = s3.list_buckets()

# Iterate over Buckets from .list_buckets() response
for bucket in response['Buckets']:
  
  	# Print the Name for each bucket
    print(bucket['Name'])


### Deleting a bucket

# Delete the gim-test bucket
s3.delete_bucket(Bucket='gim-test')

# Get the list_buckets response
response = s3.list_buckets()

# Print each Buckets Name
for bucket in response['Buckets']:
    print(bucket['Name'])


### Deleting multiple buckets

# Get the list_buckets response
response = s3.list_buckets()

# Delete all the buckets with 'gim', create replacements.
for bucket in response['Buckets']:
  if 'gim' in bucket['Name']:
      s3.delete_bucket(Bucket=bucket['Name'])
    
s3.create_bucket(Bucket='gid-staging')
s3.create_bucket(Bucket='gid-processed')
  
# Print bucket listing after deletion
response = s3.list_buckets()
for bucket in response['Buckets']:
    print(bucket['Name'])


### Putting files in the cloud

# Upload final_report.csv to gid-staging
s3.upload_file(Filename='final_report.csv',
              # Set filename and key
               Bucket='gid-staging', 
               Key='2019/final_report_01_01.csv')

# Get object metadata and print it
response = s3.head_object(Bucket='gid-staging', 
                       Key='2019/final_report_01_01.csv')

# Print the size of the uploaded object
print(response['ContentLength'])


### Spring cleaning

# List only objects that start with '2018/final_'
response = s3.list_objects(Bucket='gid-staging', 
                           Prefix='2018/final_')

# Iterate over the objects
if 'Contents' in response:
  for obj in response['Contents']:
      # Delete the object
      s3.delete_object(Bucket='gid-staging', Key=obj['Key'])

# Print the remaining objects in the bucket
response = s3.list_objects(Bucket='gid-staging')

for obj in response['Contents']:
  	print(obj['Key'])

