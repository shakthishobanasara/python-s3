import boto3
 
s3 = boto3.client("s3")
 
def upload_file():
    s3.put_object(
        Bucket="my-app-bucket",
        Key="hello.txt",
        Body="Hello from EKS"
    )
