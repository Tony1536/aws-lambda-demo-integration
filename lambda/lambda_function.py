import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('clients')  

def lambda_handler(event, context):
    method = event['httpMethod']

    if method == "POST":
        body = json.loads(event['body'])
        table.put_item(Item=body)
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps("Client registered successfully")
        }

    elif method == "GET":
        client_id = event['pathParameters']['clientsID']
        response = table.get_item(Key={'clientsID': client_id})
        item = response.get('Item')
        if item:
            return {
                "statusCode": 200,
                "headers": {
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps(item)
            }
        else:
            return {
                "statusCode": 404,
                "headers": {
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps("Client not found")
            }

    return {
        "statusCode": 400,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps("Unsupported method")
    }
