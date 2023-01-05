from rest_framework.viewsets import ModelViewSet
from opening_hours.serializers import Opening_HoursSerializer
from  opening_hours.models import Opening_Hours

class Opening_HoursViewset(ModelViewSet):
    queryset=Opening_Hours.objects.all()
    serializer_class=Opening_HoursSerializer