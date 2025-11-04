import os
import sys
from dotenv import load_dotenv
from cloudfs_oci import OCICloudFs

oci_config_path = "~/.oci/config"
oci_bucket = "bucket-c2pa-test"
oci_namespace = "axvcbsiy74ty"
def test_upload(oci_file_path, local_file_path):
    fs = OCICloudFs(oci_namespace, oci_bucket, oci_config_path)
    dir_list = fs.list('/')
    print(f"Directory list:{dir_list}")
    try:
        print(f"Downloading file {oci_file_path} -> {local_file_path}")
        fs.download_file(oci_file_path, local_file_path)
        print('Download file : PASS')
    except Exception as e:
        print('Download file: FAIL', e)

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <oci_file_path> <local_file_path>")
        exit

    test_upload(sys.argv[1], sys.argv[2])

