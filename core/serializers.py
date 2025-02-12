from rest_framework import serializers
from .models import Customer,Orders

class CreateCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Customer
        fields=["name","email"]

class CreateOrdersSerializer(serializers.ModelSerializer):
    # customer=CreateCustomerSerializer()
    class Meta:
        model=Orders
        fields=["product_name","amount","created_at","customer"]
