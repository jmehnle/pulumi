import pulumi
import pulumi_aws as aws
import pulumi_pulumi as pulumi

provider = pulumi.providers.Aws("bucket", region="us-west-2")
bucket1 = aws.s3.Bucket("bucket", opts=pulumi.ResourceOptions(provider=provider,
    depends_on=[provider],
    protect=True,
    ignore_changes=[
        "bucket",
        "lifecycleRules[0]",
    ]))
