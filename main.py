import cdktf
from stacks.r2_bucket_stack import R2BucketStack

app = cdktf.App()

R2BucketStack(
    app,
    "R2BucketStack",
)

app.synth()
