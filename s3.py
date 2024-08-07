#!/usr/bin/env python3

import boto3


class S3BucketLister:
    def __init__(self, region_name=None):
        self.session = boto3.Session(
            region_name=us-east-2,
            aws_access_key="AKIA2UC3BSXMPKKZ6I57",
            aws_secret_access_key="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",
        )
        self.s3 = self.session.client("s3")

    def list_buckets(self):
        response = self.s3.list_buckets()
        buckets = [bucket["Name"] for bucket in response["Buckets"]]
        return buckets


if __name__ == "__main__":
    bucket_lister = S3BucketLister(region_name="us-east-1")
    buckets = bucket_lister.list_buckets()
    print(buckets)
