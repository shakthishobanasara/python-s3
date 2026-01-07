import os
import boto3
from botocore.exceptions import ClientError

def create_file(file_name, content):
    with open(file_name, 'w') as f:
        f.write(content)
    print(f"File {file_name} created with content.")

def upload_file_to_s3(file_name, bucket_name, object_name=None):
    if object_name is None:
        object_name = file_name

    s3_client = boto3.client('s3')

    try:
        s3_client.upload_file(file_name, bucket_name, object_name)
    except ClientError as e:
        print(f"Client error: {e}")
        return False

    print(f"File {file_name} uploaded to {bucket_name}/{object_name}")
    return True

if __name__ == "__main__":
    file_name = "runtime_file.txt"
    content = "This file was created at runtime and will be uploaded to S3."

    bucket_name = os.getenv('S3_BUCKET_NAME')
    if not bucket_name:
        raise ValueError("Environment variable S3_BUCKET_NAME is not set")

    create_file(file_name, content)
    upload_file_to_s3(file_name, bucket_name)
