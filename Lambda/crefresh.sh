#!/bin/bash
aws s3 cp ~/Python/CloudFormation.yaml s3://cf-templates-18fwx0sfsoz9r-ap-southeast-2/
aws cloudformation delete-stack --stack-name S3ListTemplate
aws cloudformation create-stack --stack-name S3ListTemplate --template-url https://s3-ap-southeast-2.amazonaws.com/cf-templates-18fwx0sfsoz9r-ap-southeast-2/CloudFormation.yaml

