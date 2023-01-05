from rest_framework import serializers
from place.models import Place
from opening_hours.models import Opening_Hours

class Opening_HoursSerializerforPlace(serializers.ModelSerializer):
    class Meta:
        model= Opening_Hours
        fields ='__all__'


class PlaceSerializer(serializers.ModelSerializer):
    openings_hourss_data = Opening_HoursSerializerforPlace(source='opening_hours', many=True)
    class Meta:
        model= Place  
        #fields ='__all__'
        exclude = ['opening_hours',]