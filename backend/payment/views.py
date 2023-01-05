from rest_framework.viewsets import ModelViewSet
from payment.serializers import PaymentSerializer
from payment.models import Payment
from authentication.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class PaymentViewset(ModelViewSet):
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer

    @action (methods=['POST'],detail= False,permission_classes=[IsAuthenticated],url_path="toggle-payment")
    def toggle_payment(self, request,pk=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'added'})
           
            