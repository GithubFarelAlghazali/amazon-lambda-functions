import json
import boto3
client = boto3.client('sns')
def lambda_handler(event, context):
   s3 = boto3.client('s3')
   file_key = event['Records'][0]['s3']['object']['key']
   filename = file_key.split('/')[-1]
   
   response = client.publish(TopicArn='arn:aws:sns:us-east-1:891377105404:s3change',Message= filename , Subject="Objek baru berhasil ditambahkan")
   print("Message published")
   return(response)

