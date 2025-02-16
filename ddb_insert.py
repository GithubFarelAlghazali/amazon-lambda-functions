import boto3

def lambda_handler(event, context):
  # Get the DynamoDB client
  dynamodb = boto3.client('dynamodb')

  # Define the item data
  item = {
  "Judul": {
    "S": "Naruto"
  },
  "Jenis": {
    "S": "Komik"
  }
}
  # Insert the item into DynamoDB
  try:
      dynamodb.put_item(TableName="DaftarBuku", Item=item)
      return {
          'statusCode': 200,
          'body': 'Item inserted successfully!'
      }
  except Exception as e:
      return {
          'statusCode': 500,
          'body': f'Error inserting item: {e}'
      }
