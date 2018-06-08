import boto3
from boto3.s3.transfer import S3Transfer
import urllib2
import os


def upload(url, foldername, postid):
    filename = url.split('/')[-1]
    u = urllib2.urlopen(url)

    f = open(filename, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (filename, file_size)

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print status,


    AWS_APP_ID = "AKIAI6RJWKRQOHDJ2PXA"
    AWS_APP_SECRET = "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"
    AWS_REGION = "ap-northeast-2"
    AWS_BUCKET = "placeness"

    f.close()

    transfer = S3Transfer(boto3.client('s3', AWS_REGION, aws_access_key_id=AWS_APP_ID, aws_secret_access_key=AWS_APP_SECRET))
    transfer.upload_file(filename, AWS_BUCKET, "instagram_dataset/" +foldername+"/"+postid)

    os.remove(filename)