from rest_framework.viewsets import ModelViewSet
from rent.serializers import RentSerializer
from rent.models import Rent
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class RentViewset(ModelViewSet):
    queryset=Rent.objects.all()
    serializer_class=RentSerializer

  
        
        


