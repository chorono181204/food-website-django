# serializers.py
from rest_framework import serializers
class CartDetailsSerializer(serializers.Serializer):
    ids = serializers.ListField(child=serializers.IntegerField())
    quantities = serializers.ListField(child=serializers.IntegerField())
class DeleteCartDetailsSerializer(serializers.Serializer):
    id=serializers.IntegerField()
class AddToCartDetailsSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    quantity=serializers.IntegerField()