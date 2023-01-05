from rest_framework.viewsets import ModelViewSet
from place.serializers import PlaceSerializer
from place.models import Place
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class PlaceViewset(ModelViewSet):
    queryset=Place.objects.all()
    serializer_class=PlaceSerializer

    @action (methods=['POST'],detail= False,permission_classes=[IsAuthenticated],url_path="toggle-place")
    def toggle_payment(self, request,pk=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'added'})
           