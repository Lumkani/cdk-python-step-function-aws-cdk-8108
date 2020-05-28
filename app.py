#!/usr/bin/env python3

from aws_cdk import core

from cdk.hello_cdk_python_stack import StepFunctionDynamoDBStack


app = core.App()
StepFunctionDynamoDBStack(app, "step-function-dynamo-db-put-item")

app.synth()
