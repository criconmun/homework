import boto3, decimal

dynamodb = boto3.resource('dynamodb', region_name='eu-west-1', endpoint_url="https://dynamodb.eu-west-1.amazonaws.com")
table = dynamodb.Table('homework')


def count():
    response = table.get_item(
        Key={
            'counter': 'mainpage'
        }
    )
    return response['Item']['visits']


def increment():
    table.update_item(
        Key={
            'counter': 'mainpage',
        },
        UpdateExpression="set visits = visits + :val",
        ExpressionAttributeValues={
            ':val': decimal.Decimal(1)
        }
    )
    return


def reset():
    table.update_item(
        Key={
            'counter': 'mainpage',
        },
        UpdateExpression="set visits = :v",
        ExpressionAttributeValues={
            ':v': decimal.Decimal(0)
        }
    )
    return
