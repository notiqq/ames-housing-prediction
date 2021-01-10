import boto3

dynamodb_url = "http://localhost:8000"
connection = boto3.resource("dynamodb", endpoint_url=dynamodb_url)