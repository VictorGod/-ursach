from rest_framework.viewsets import ModelViewSet
from rent.serializers import RentSerializer
from rent.models import Rent
from authentication.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend




class RentViewset(ModelViewSet):
    queryset=Rent.objects.all()
    serializer_class=RentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['client_id', 'place', 'payment']

    @action (methods=['POST'],detail= False,permission_classes=[IsAuthenticated],url_path="toggle-rent")
    def toggle_rent(self, request,pk=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'added'})
    @action (methods=['GET'],detail= False,permission_classes=[IsAuthenticated],url_path="list_rent")
    def get_payment(self, request):
       client_id=request.user
    #    payment = request.data.payment
    #    rent = Rent.objects.filter(payment=payment)
       rent = Rent.objects.filter(client_id=client_id)
       data=RentSerializer(instance=rent,many = True).data
       return Response(data)
    
    

    
        
        




           
           

  
        
        


