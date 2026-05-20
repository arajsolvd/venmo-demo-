from aws_cdk import Stack, aws_s3 as s3, RemovalPolicy
from constructs import Construct


class VenmoDemoStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        s3.Bucket(
            self,
            "VenmoDemoBucket",
            versioned=False,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
            public_read_access=False,
        )
