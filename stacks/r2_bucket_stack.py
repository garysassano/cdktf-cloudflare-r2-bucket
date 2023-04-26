import os
from cdktf import TerraformStack
from cdktf_cdktf_provider_aws.provider import (
    AwsProvider,
    AwsProviderEndpoints,
)
from cdktf_cdktf_provider_aws.s3_bucket import S3Bucket
from constructs import Construct


class R2BucketStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        CLOUDFLARE_ACCOUNT_ID = os.environ.get("CLOUDFLARE_ACCOUNT_ID")
        CLOUDFLARE_R2_ACCESS_KEY = os.environ.get("CLOUDFLARE_R2_ACCESS_KEY")
        CLOUDFLARE_R2_SECRET_KEY = os.environ.get("CLOUDFLARE_R2_SECRET_KEY")

        r2_endpoint = AwsProviderEndpoints(
            s3=f"https://{CLOUDFLARE_ACCOUNT_ID}.r2.cloudflarestorage.com",
        )

        AwsProvider(
            self,
            "AwsProvider_emulated-cloudflare-provider",
            region="auto",
            access_key=CLOUDFLARE_R2_ACCESS_KEY,
            secret_key=CLOUDFLARE_R2_SECRET_KEY,
            skip_credentials_validation=True,
            skip_region_validation=True,
            skip_requesting_account_id=True,
            endpoints=[r2_endpoint],
        )

        r2_bucket = S3Bucket(
            self,
            "R2Bucket_test-bucket",
            bucket="test-bucket",
        )
