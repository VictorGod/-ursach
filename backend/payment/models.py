from django.db import models
from authentication.models import User

class Payment (models.Model):
    client_id = models.ManyToManyField(to = User, related_name="payment" )
    data = models.DateField(verbose_name='')
def __str__(self):
        return self.data

class Meta:
        verbose_name = 'оплата'
        verbose_name_plural = 'оплата'


   