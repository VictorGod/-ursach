from rest_framework import serializers
from opening_hours.models import Opening_Hours

class Opening_HoursSerializer(serializers.ModelSerializer):
    class Meta:
        model= Opening_Hours
        fields ='__all__'