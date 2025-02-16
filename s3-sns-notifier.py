import json
import boto3
client = boto3.client('sns')
def lambda_handler(event, context):
   s3 = boto3.client('s3')
   # Extract filename from S3 object key
   file_key = event['Records'][0]['s3']['object']['key']
   filename = file_key.split('/')[-1]
    # Define the item data (corrected filename and timestamp format)
   item = {
        "Filename": {
            "S": filename
        }
    }
   
   response = client.publish(TopicArn=(your-sns-arn),Message= item , Subject="Objek baru berhasil ditambahkan")
   print("Message published")
   return(response)

