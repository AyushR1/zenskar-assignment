from rest_framework import generics
from .models import Customer
from .serializers import CustomerSerializer, StripeWebhookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class StripeWebhookView(APIView):
    def post(self, request, format=None):
        print('Received Stripe webhook')
        serializer = StripeWebhookSerializer(data=request.data)
        if serializer.is_valid():
            event_id = serializer.validated_data['id']
            event_type = serializer.validated_data['type']
            customer_data = serializer.validated_data['data']
            print('Received Stripe webhook with id={} and type={}'.format(event_id, event_type))
            print(customer_data)
            if (event_type=='customer.created'):
                customer_id = customer_data['object']['id']
                customer_name = customer_data['object']['name']
                customer_email = customer_data['object']['email']

                if not Customer.objects.filter(email=customer_email).exists():
                    customer = Customer(id=customer_id, name=customer_name, email=customer_email)
                    customer.save()
                    print('Created customer with email={}'.format(customer_email))
                else:
                    print('Customer with email={} already exists'.format(customer_email))

                return Response(status=status.HTTP_200_OK)
            elif (event_type=='customer.deleted'):
                customer_email = customer_data['object']['email']

                if Customer.objects.filter(email=customer_email).exists():
                    customer = Customer.objects.get(email=customer_email)
                    customer.delete()
                    print('Deleted customer with email={}'.format(email=customer_email))
                else:
                    print('Customer with email={} does not exist'.format(email=customer_email))

                return Response(status=status.HTTP_200_OK)
            else:
                print('Unknown event type {}'.format(event_type))
                return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
