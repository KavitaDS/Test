from __future__ import print_function #
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="https://dynamodb.us-west-2.amazonaws.com")


table = dynamodb.create_table(
    TableName='BluekaiAudienceIdType',
    KeySchema=[
        {
            'AttributeName': 'audience_id',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'audience_type',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'audience_id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'audience_type',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)
