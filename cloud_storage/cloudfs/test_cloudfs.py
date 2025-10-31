import os
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

def test_cloudfs_file_operations():
    print(f"[INFO] Using S3_URI: {S3_URI}")
    print(f"[INFO] AWS_ACCESS_KEY_ID: {AWS_ACCESS_KEY_ID}")
    print(f"[INFO] AWS_REGION: {AWS_REGION}")
    fs = CloudFs(S3_URI, **S3_OPTS)
    try:
        print("[INFO] Uploading file 'test_file_140mb.bin -> dest_files/test_file_140mb.bin'")
        fs.upload_file('dest_files/test_file_140mb.bin', './test_file_140mb.bin')
        print("[INFO] Downloading file 'src_files/test_file_140mb.bin -> test_file_140mb.bin'")
        fs.download_file('src_files/test_file_140mb.bin', './test_file_140mb.bin')
        #print("[INFO] Deleting file 'docs/hello.txt'")
        #fs.delete('docs/hello.txt')
        #print("[INFO] Listing files in 'docs' after deletion")
        #try:
        #    files_after = fs.list('docs')
        #    print(f"[INFO] Files in 'docs' after deletion: {files_after}")
        #    txt_files = [f for f in files_after if f.endswith('.txt')]
        #    print(f"[INFO] .txt files in 'docs' after deletion: {txt_files}")
        #    assert not txt_files
        #except Exception as e:
        #    print(f"[INFO] Listing 'docs' after deletion raised exception (expected if folder is gone): {e}")
        print('test_cloudfs_file_operations: PASS')
    except Exception as e:
        print('test_cloudfs_file_operations: FAIL', e)
    #finally:
    #    print("[INFO] Cleaning up: deleting 'docs' folder")
    #    try:
    #        fs.delete('docs', recursive=True)
    #    except Exception as ce:
    #        print(f"[WARN] Cleanup failed: {ce}")

if __name__ == '__main__':
    test_cloudfs_file_operations()
