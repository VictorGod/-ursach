from django.db import models
from authentication.models import User
from landlord.models import LandLord
from place.models import Place
from payment.models import Payment


class Rent (models.Model):
    client_id = models.ManyToManyField(to = User, related_name="Rent" )
    landlord_id = models.ManyToManyField(to = LandLord, related_name="Rent" )
    start_data = models.DateField(verbose_name='начало аредны')
    end_data=models.CharField(verbose_name="конец аредны",max_length=255)
    place = models.ManyToManyField(to = Place, related_name="Rent" ) 
    payment = models.ManyToManyField(to = Payment, related_name="Rent" ) 
def __str__(self):
        return self.data

class Meta:
        verbose_name = 'Аренда'
        verbose_name_plural = 'Аренда'


   