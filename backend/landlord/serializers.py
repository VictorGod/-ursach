from rest_framework import serializers
from landlord.models import LandLord
from place.models import Place

class PlaceSerializerforLandLord(serializers.ModelSerializer):
    class Meta:
        model= Place 
        fields ='__all__'

class LandLordSerializer(serializers.ModelSerializer):
    places_data = PlaceSerializerforLandLord(source='place', many=True)
    class Meta:
        model= LandLord 
        #fields ='__all__'
        exclude = ['place',]