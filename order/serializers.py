from rest_framework import serializers
class OrderSerializer(serializers.Serializer):
    name = serializers.CharField()
    address = serializers.CharField()
    phone = serializers.CharField()
    note = serializers.CharField()