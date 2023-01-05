from rest_framework import serializers
from payment.models import Payment
from authentication.serializers import UserSerializer,User


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Payment
        fields ='__all__'