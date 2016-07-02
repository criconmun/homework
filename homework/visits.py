import boto3
import decimal

from homework import appsettings

dynamodb = boto3.resource('dynamodb',
                          region_name=appsettings.dynamodb_region,
                          endpoint_url=appsettings.dynamodb_endpoint)

table = dynamodb.Table(appsettings.dynamodb_table)


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
