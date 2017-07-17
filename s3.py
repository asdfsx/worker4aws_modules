import boto3
import os


def objectcreate(jobid, params):
    bucket_name = params["bucket_name"]["S"]
    bucket_arn = params["bucket_arn"]["S"]
    object_key = params["object_key"]["S"]
    object_size = params["object_size"]["N"]

    if bucket_name == "arn:aws:s3:::mybucket":
        return

    path = os.path.dirname(object_key)
    dest_path = os.path.join(".", path)
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    filename = os.path.basename(object_key)
    dest_file = os.path.join(dest_path, filename)

    client = boto3.client("s3")
    client.download_file(bucket_name, object_key, dest_file)
