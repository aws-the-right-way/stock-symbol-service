#!/bin/bash

AWS_ECR_URI="${AWS_ECR_URI}"

aws configure set default.region eu-central-1

$(aws ecr get-login --no-include-email)

docker tag stock-symbol-service:0.1 $AWS_ECR_URI:0.1
docker push $AWS_ECR_URI:0.1
