def handler(event, context):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/plain; charset=utf-8"},
        "body": "hello world after multiple tries"
    }