import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Inventory')

def lambda_handler(event, context):
    item_id = event['pathParameters']['id']
    response = table.get_item(Key={'item_id': item_id})
    item = response.get('Item')
    if not item:
        return { 'statusCode': 404, 'body': 'Item not found' }
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }
