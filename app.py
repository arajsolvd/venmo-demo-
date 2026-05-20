#!/usr/bin/env python3
import aws_cdk as cdk

from venmo_demo.venmo_demo_stack import VenmoDemoStack

app = cdk.App()
VenmoDemoStack(app, "VenmoDemoStack")

app.synth()
