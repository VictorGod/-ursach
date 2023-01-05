from rest_framework.viewsets import ModelViewSet
from landlord.serializers import LandLordSerializer
from landlord.models import LandLord

class LandLordViewset(ModelViewSet):
    queryset=LandLord.objects.all()
    serializer_class=LandLordSerializer