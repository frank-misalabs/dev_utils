import os
import sys
from dotenv import load_dotenv
from cloudfs import CloudFs

# Load S3 config from .env
load_dotenv()
S3_URI = os.getenv("S3_URI")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

S3_OPTS = {
    "key": AWS_ACCESS_KEY_ID,
    "secret": AWS_SECRET_ACCESS_KEY,
    "client_kwargs": {"region_name": AWS_REGION}
}

def test_upload(s3_file_path, local_file_path):
    print(f"[INFO] Using S3_URI: {S3_URI}")
    print(f"[INFO] AWS_ACCESS_KEY_ID: {AWS_ACCESS_KEY_ID}")
    print(f"[INFO] AWS_REGION: {AWS_REGION}")
    fs = CloudFs(S3_URI, **S3_OPTS)
    try:
        print(f"[INFO] Uploading file {local_file_path} -> {S3_URI}/{s3_file_path}")
        fs.upload_file(s3_file_path, local_file_path)
        print('Upload file : PASS')
    except Exception as e:
        print('Upload file: FAIL', e)

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <s3_file_path> <local_file_path>")
        exit

    test_upload(sys.argv[1], sys.argv[2])

