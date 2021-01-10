import boto3
from boto3.dynamodb.conditions import Key
from config import connection


def create_objects_table():
    table = connection.create_table(
        TableName='Objects',
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'N'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1,
        }
    )
    print("Table status:", table.table_status)

def create_real_estate_object(real_estate_object):
    table = connection.Table('Objects')
    response = table.put_item(
       Item=real_estate_object
    )
    return response