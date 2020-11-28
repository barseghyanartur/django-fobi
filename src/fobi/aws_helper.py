import mimetypes
import boto3
from botocore.exceptions import ClientError, NoCredentialsError
import uuid
from django.conf import settings
import os

ACCESS_KEY = settings.AWS_ACCESS_KEY_ID
SECRET_KEY = settings.AWS_SECRET_ACCESS_KEY
BUCKET_NAME = settings.AWS_STORAGE_BUCKET_NAME
REGION_NAME = settings.AWS_S3_REGION_NAME


def aws_connection():
    return boto3.client(
        "s3", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY
    )


def file_exist(destination):
    connection = aws_connection()
    try:
        connection.head_object(Bucket=BUCKET_NAME, Key=destination)
    except ClientError as e:
        return int(e.response["Error"]["Code"]) != 404
    return True


def ensure_unique_file(destination):
    if file_exist(destination):
        filename, extension = os.path.splitext(destination)
        return "{0}_{1}{2}".format(filename, uuid.uuid4(), extension)
    return destination


def upload_file(local_file, s3_file, bucket=BUCKET_NAME):
    connection = aws_connection()
    try:
        connection.upload_file(
            local_file,
            bucket,
            s3_file,
            ExtraArgs={
                "ContentType": mimetypes.guess_type(local_file)[0],
                "ACL": "public-read",
            },
        )
        return True
    except FileNotFoundError:
        return False
    except NoCredentialsError:
        return False
