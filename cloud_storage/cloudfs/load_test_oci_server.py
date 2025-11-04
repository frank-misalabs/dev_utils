# This is the XML RPC server that performs the cloud file read and write
# This is needed as fsspec sync does not work within Locust coroutine
# An extra XMLRPC layer is needed to wrap the cloudfs (using fsspec)
# upload/download functions

import random
import os
import sys
from dotenv import load_dotenv
from cloudfs_oci import OCICloudFs
from xmlrpc.server import SimpleXMLRPCServer

oci_config_path = "~/.oci/config"
oci_bucket = "bucket-c2pa-test"
oci_namespace = "axvcbsiy74ty"

fs = OCICloudFs(oci_namespace, oci_bucket, oci_config_path)
port = None

# It is important to choose a high performance block volume to keep low latency and variation
# of file read/write throughput. Please change to a different path that you've mounted for
# a folder in the high performance volume
local_base_path = "/mnt/data2/test_data"


def upload_large_file():
    oci_file_path = "dest_files/test_file_upload_140mb_" + port + ".bin"
    local_file_path = local_base_path + "/test_file_upload_140mb.bin"

    try:
        #print(f"[INFO] Uploading file {local_file_path} -> {oci_file_path}")
        fs.upload_file(oci_file_path, local_file_path)
        #print('Upload file done')
    except Exception as e:
        print('Upload file fail', e)

    return True

def upload_small_file():
    oci_file_path = "dest_files/test_file_upload_8mb_" + port + ".bin"
    local_file_path = local_base_path + "/test_file_upload_8mb.bin"

    try:
        #print(f"[INFO] Uploading file {local_file_path} -> {oci_file_path}")
        fs.upload_file(oci_file_path, local_file_path)
        #print('Upload file done')
    except Exception as e:
        print('Upload file fail', e)

    return True

def download_large_file():
    oci_file_path = "src_files/test_file_140mb.bin"
    local_file_path = local_base_path + "/test_file_140mb_" + port + ".bin"

    try:
        #print(f"[INFO] Downloading file {oci_file_path} --> {local_file_path}")
        fs.download_file(oci_file_path, local_file_path)
        #print('Download file done')
    except Exception as e:
        print('Download file fail', e)

    return True

def download_small_file():
    oci_file_path = "src_files/test_file_8mb.bin"
    local_file_path = local_base_path + "/test_file_8mb_" + port + ".bin"

    try:
        #print(f"[INFO] Downloading file {oci_file_path} --> {local_file_path}")
        fs.download_file(oci_file_path, local_file_path)
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
