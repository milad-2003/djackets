from rest_framework import serializers

from .models import Order, OrderItem

from product.serializers import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            "price",
            "product",
            "quantity",
        )

    def validate(self, data):
        product = data.get('product')
        if not product:
            raise serializers.ValidationError("Invalid product.")
        return data


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "zipcode",
            "place",
            "phone",
            "stripe_token",
            "items",
        )

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        
        return order

    def validate(self, data):
        if not data.get('items'):
            raise serializers.ValidationError("Order must contain at least one item.")
        return data
    