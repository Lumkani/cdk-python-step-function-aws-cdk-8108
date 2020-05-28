#!/usr/bin/env python3

from aws_cdk import core

from hello_cdk_python.hello_cdk_python_stack import HelloCdkPythonStack


app = core.App()
HelloCdkPythonStack(app, "hello-cdk-python")

app.synth()
