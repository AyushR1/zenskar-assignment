from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .kafka import send_to_kafka, create_customer_event, EVENT_CUSTOMER_CREATED, EVENT_CUSTOMER_DELETED
import json


class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

@receiver(post_save, sender=Customer)
def customer_saved(sender, instance, **kwargs):
    action = EVENT_CUSTOMER_CREATED
    event = create_customer_event(action, instance)
    send_to_kafka('customer_events', json.dumps(event).encode('utf-8'))

@receiver(post_delete, sender=Customer)
def customer_deleted(sender, instance, **kwargs):
    event = create_customer_event(EVENT_CUSTOMER_DELETED, instance)
    send_to_kafka('customer_events', json.dumps(event).encode('utf-8'))