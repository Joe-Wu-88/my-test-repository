import os

def lambda_handler(event, context):
    request = event['Records'][0]['cf']['request']
    originDomain = os.environ['originDomain']
    request['headers']['host'][0]['value'] = originDomain;
    return request
