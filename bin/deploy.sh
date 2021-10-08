#!/bin/bash

set -e

export AWS_DEFAULT_REGION=${AWS_DEFAULT_REGION:=us-east-1}
export TEMPLATE_FILE="template.yml"
export OUTPUT_TEMPLATE_FILE="template-packaged.yml"
export APP="ctl"

sam package \
  --region ${AWS_DEFAULT_REGION} \
  --template-file ${TEMPLATE_FILE} \
  --output-template-file ${OUTPUT_TEMPLATE_FILE}

sam deploy \
  --region ${AWS_DEFAULT_REGION} \
  --template-file ${OUTPUT_TEMPLATE_FILE} \
  --stack-name ${APP} \
  --capabilities "CAPABILITY_IAM" \
  --tags \
    "application=${APP}"
