def lambda_handler(event, context):
    try:
        number = int(event.get("number"))
        result = 100 / number

        return {
            "statusCode": 200,
            "body": f"Result is {result}"
        }

    except Exception as e:
        return {
            "statusCode": 400,
            "body": f"Error occurred: {str(e)}"
        }