from rest_framework.filters import SearchFilter, OrderingFilter, BaseFilterBackend
from rest_framework.viewsets import ModelViewSet
from .serializers import CustomerSerializer
from .models import Customer
from django_filters.rest_framework import DjangoFilterBackend


class CustomerViewSet(ModelViewSet):
    model = Customer
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["id","first_name"]
