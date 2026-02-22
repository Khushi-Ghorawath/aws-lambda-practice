import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('YourTableName')

def lambda_handler(event, context):
    response = table.put_item(
        Item={
            'id': '1',
            'message': 'Hello from DynamoDB'
        }
    )

    return {
        "statusCode": 200,
        "body": "Item inserted successfully!"
    }