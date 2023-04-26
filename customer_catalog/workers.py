from confluent_kafka import Consumer, KafkaError
import stripe
import json

EVENT_CUSTOMER_CREATED = 'customer_created'
EVENT_CUSTOMER_DELETED = 'customer_deleted'

stripe.api_key = "sk_test_51N0zLmSHwOQnP5vgOAGX9zaGDf0xG1Lfz64QX01jtWu30YDjubo8fnSJjeooeXo9A4RnrX18j3n2WRVx3IuCG5GP001H2wGFNp"

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest'
})


def process_message(msg):
    event = json.loads(msg.value())
    if event['action'] == EVENT_CUSTOMER_CREATED:
        stripe.Customer.create(
            id=event['customer_id'],
            name=event['customer_name'],
            email=event['customer_email']
        )
        print("created")
    elif event['action'] == EVENT_CUSTOMER_DELETED:
        stripe.Customer.delete(str(event['customer_id']))
        print("deleted")

consumer.subscribe(['customer_events'])

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue

    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print('End of partition reached')
        else:
            print('Error while consuming message: {}'.format(msg.error()))
    else:
        print('Received message: {}'.format(msg.value()))
        process_message(msg)
    consumer.commit()

consumer.close()
