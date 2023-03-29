import boto3

# Create an SQS client
sqs = boto3.client('sqs')

# Set up the queue attributes
queue_name = 'my-queue'
queue_attributes = {
    'DelaySeconds': '0',
    'VisibilityTimeout': '30'
}

# Create the queue
response = sqs.create_queue(
    QueueName=queue_name,
    Attributes=queue_attributes
)

# Print the URL of the newly created queue
print(f'Queue created: {response["QueueUrl"]}')

def send_message_to_sqs(message):
    response = queue.send_message(MessageBody=message)
    print(f"Message sent with ID: {response['MessageId']}")


send_message_to_sqs("Hello, world!")