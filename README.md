# venmo-demo

A Python AWS CDK app scaffold for a Venmo-style payments demo, built to show a serverless backend design.

Repository: https://github.com/arajsolvd/venmo-demo-.git

## Setup

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Synthesize the CloudFormation template:
   ```bash
   cdk synth
   ```

> Note: The AWS CDK CLI must be installed separately to run `cdk synth`.
