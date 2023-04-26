from confluent_kafka import Producer

EVENT_CUSTOMER_CREATED = 'customer_created'
EVENT_CUSTOMER_DELETED = 'customer_deleted'


producer = Producer({
    'bootstrap.servers': 'localhost:9092'
})

def send_to_kafka(topic, data):
    producer.produce(topic, key=None, value=data)
    producer.flush()


def create_customer_event(action, customer):
    return {
        'action': action,
        'customer_id': customer.id,
        'customer_name': customer.name,
        'customer_email': customer.email
    }
