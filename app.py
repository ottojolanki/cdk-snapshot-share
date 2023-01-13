import os

from aws_cdk import App
from aws_cdk import Duration
from aws_cdk import Environment
from aws_cdk import Stack

from aws_cdk.aws_lambda_python_alpha import PythonFunction
from aws_cdk.aws_lambda import Runtime

from aws_cdk.aws_iam import PolicyStatement
from aws_cdk.aws_iam import Role

from constructs import Construct

from typing import Any

IGVF_DEV_ENV = Environment(account='109189702753', region='us-west-2')

class LatestSnapshotLambda(Stack):

    def __init__(
            self,
            scope: Construct,
            construct_id: str,
            **kwargs: Any
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.get_latest_snapshot_id = PythonFunction(
            self,
            'GetLatestSnapshotID',
            entry='lambda/',
            runtime=Runtime.PYTHON_3_9,
            index='main.py',
            handler='get_latest_snapshot_id',
            timeout=Duration.seconds(60),
        )
        self.get_latest_snapshot_id.add_to_role_policy(
             PolicyStatement(
                actions=['rds:DescribeDBSnapshots'],
                resources=['*'],
            )
        )


app = App()

latest_snapshot_lambda = LatestSnapshotLambda(app, 'LatestSnapshotLambda', env=IGVF_DEV_ENV)

app.synth()
