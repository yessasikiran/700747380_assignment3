import boto3
import configparser

config = configparser.ConfigParser()
config.read('my-queue.ini')

queue_name = config['default']['queue_name']
sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName=queue_name)

def send_message_to_sqs(message):
    response = queue.send_message(MessageBody=message)
    print(f"Message sent with ID: {response['MessageId']}")
