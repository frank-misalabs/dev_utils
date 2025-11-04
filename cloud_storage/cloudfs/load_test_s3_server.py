import random
import os
import sys
from dotenv import load_dotenv
from cloudfs import CloudFs
from xmlrpc.server import SimpleXMLRPCServer

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

print(f"[INFO] Using S3_URI: {S3_URI}")
print(f"[INFO] AWS_ACCESS_KEY_ID: {AWS_ACCESS_KEY_ID}")
print(f"[INFO] AWS_REGION: {AWS_REGION}")
fs = CloudFs(S3_URI, **S3_OPTS)

def upload_large_file():
    s3_file_path = "dest_files/test_file_upload_140mb.bin"
    local_file_path = "/mnt/data2/test_data/test_file_upload_140mb.bin"

    try:
        #print(f"[INFO] Uploading file {local_file_path} -> {S3_URI}/{s3_file_path}")
        fs.upload_file(s3_file_path, local_file_path)
        #print('Upload file done')
    except Exception as e:
        print('Upload file fail', e)

    return True

def upload_small_file():
    s3_file_path = "dest_files/test_file_upload_8mb.bin"
    local_file_path = "/mnt/data2/test_data/test_file_upload_8mb.bin"

    try:
        #print(f"[INFO] Uploading file {local_file_path} -> {S3_URI}/{s3_file_path}")
        fs.upload_file(s3_file_path, local_file_path)
        #print('Upload file done')
    except Exception as e:
        print('Upload file fail', e)

    return True

def download_large_file():
    s3_file_path = "src_files/test_file_140mb.bin"
    local_file_path = "/mnt/data2/test_data/test_file_140mb_" + port + ".bin"

    try:
        #print(f"[INFO] Downloading file {S3_URI}/{s3_file_path} --> {local_file_path}")
        fs.download_file(s3_file_path, local_file_path)
        #print('Download file done')
    except Exception as e:
        print('Download file fail', e)

    return True

def download_small_file():
    s3_file_path = "src_files/test_file_8mb.bin"
    local_file_path = "/mnt/data2/test_data/test_file_8mb_" + port + ".bin"

    try:
        #print(f"[INFO] Downloading file {S3_URI}/{s3_file_path} --> {local_file_path}")
        fs.download_file(s3_file_path, local_file_path)
        #print('Download file done')
    except Exception as e:
        print('Download file fail', e)

    return True

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <port>")
        exit

    #server = SimpleXMLRPCServer(("localhost", 8877))
    server = SimpleXMLRPCServer(("localhost", int(sys.argv[1])))
    print(f"Listening on port {sys.argv[1]}...")
    port = sys.argv[1]
    server.register_function(upload_large_file, "upload_large_file")
    server.register_function(upload_small_file, "upload_small_file")
    server.register_function(download_large_file, "download_large_file")
    server.register_function(download_small_file, "download_small_file")
    server.serve_forever()
