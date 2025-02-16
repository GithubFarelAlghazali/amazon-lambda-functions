import boto3
import json
import datetime

def lambda_handler(event, context):
    # Get the DynamoDB client
    dynamodb = boto3.client('dynamodb')
    s3 = boto3.client('s3')

    # Extract filename from S3 object key
    file_key = event['Records'][0]['s3']['object']['key']
    filename = file_key.split('/')[-1]
    timestamp = datetime.datetime.now().isoformat()  # Use ISO 8601 format for timestamps

    # Define the item data (corrected filename and timestamp format)
    item = {
        "Timestamp": {
            "S": timestamp
        },
        "Filename": {
            "S": filename
        }
    }

    # Insert the item into DynamoDB
    try:
        dynamodb.put_item(TableName="S3Objects", Item=item)
        return {
            'statusCode': 200,
            'body': 'Item inserted successfully!'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error inserting item: {e}'
        }
