import json


def handler(event, context):
    # Extract query parameters if present (e.g., ?name=Developer)
    query_params = event.get('queryStringParameters') or {}
    name = query_params.get('name', 'World')

    # Construct JSON response
    response_body = {
        "message": f"Hello, {name}!",
        "status": "success"
    }

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(response_body)
    }
