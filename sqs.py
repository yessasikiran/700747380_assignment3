import boto3
import configparser

config = configparser.ConfigParser()
config.read('my-queue.ini')

queue_name = config['default']['queue_name']
sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName=queue_name)