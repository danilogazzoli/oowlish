from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    """
    Serializer class for customer's endpoint
    """
    class Meta:
        model = Customer
        fields = "__all__"

