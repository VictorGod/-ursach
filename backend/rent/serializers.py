from rest_framework import serializers
from rent.models import Rent
from payment.models import Payment

class PaymentSerializerforRent(serializers.ModelSerializer):
    class Meta:
        model= Payment
        fields ='__all__'


class RentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Rent 
        fields ='__all__'
        