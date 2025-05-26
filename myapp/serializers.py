from rest_framework import serializers
from .models import FoodItem, Order

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    customer_name = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'customer', 'food', 'quantity', 'customer_name']

    def get_customer_name(self, obj):
        # Return some custom representation of customer
        return obj.customer  # or format however you want

