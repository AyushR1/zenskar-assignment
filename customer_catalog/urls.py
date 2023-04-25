from django.urls import path
from .views import CustomerList, CustomerDetail

urlpatterns = [
    path('customers/', CustomerList.as_view(), name='customer_list'),
    path('customers/<int:pk>/', CustomerDetail.as_view(), name='customer_detail'),
]
