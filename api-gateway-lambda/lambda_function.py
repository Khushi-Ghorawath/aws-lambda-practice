import json

def lambda_handler(event, context):
    name = event.get("queryStringParameters", {}).get("name", "Guest")

    return {
        "statusCode": 200,
        "body": json.dumps(f"Hello {name}, welcome to API Gateway Lambda!")
    }