import json
import datetime


def handler(event, context):
    name = "Default"
    if event is not None and event["pathParameters"] is not None:
        name = event["pathParameters"]["name"]
    data = {
        'output': 'Hello ' + name,
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'event': event,
        'context': context
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
