# Cloud file util to perform file / dir functions on any cloud object storage

## Instruction

### Install python dependencies
```shell
pip install fsspec s3fs
```

### Create test file

On your local machine
```shell
truncate -s 140mb test_file_140mb.bin
```

On your S3 bucket
1. Create two sub-folders: dest_files and src_files
2. Upload a test file named test_file_140mb.bin to src_files


### Update .env
Setup the env var using your S3 credentials and URI
```shell
  S3_URI=s3://..<your bucket uri>
  AWS_ACCESS_KEY_ID=<your accessk key id>
  AWS_SECRET_ACCESS_KEY=<your secret key>
  AWS_REGION=<your region, e.g. us-east-1>
```

Run test
``` shell
python test_cloudfs.py
```
Then you should see the updated file on S3 and local machine
