from rest_framework import serializers

class CheckEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)
class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=100)
    id=serializers.IntegerField()