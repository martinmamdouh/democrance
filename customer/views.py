from rest_framework import viewsets
from customer.serializers import CustomerSerializer
from customer.models import Customer


class CustomerApi(viewsets.ModelViewSet):
    """
    A viewset for creating new customer instances.
    """
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
