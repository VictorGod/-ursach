from django.db import models
from place.models import Place

class LandLord (models.Model):
    work_email=models.EmailField(verbose_name="Email name",max_length=255,unique=True)
    full_name=models.CharField(verbose_name="Название компании",max_length=255)
    abbreviated_name=models.CharField(verbose_name="Абривеатура",max_length=255)
    logo=models.ImageField(verbose_name="лого",upload_to="users/photos")
    bio =models.TextField(verbose_name="о себе")
    manager_telegram_name = models.CharField(verbose_name="Телеграмм_логин",max_length=255)
    place = models.ManyToManyField(to = Place, related_name="LandLord" ) 
    address = models.TextField(verbose_name="адресс")
def __str__(self):
        return self.work_email

class Meta:
        verbose_name = 'Арендодатель'
        verbose_name_plural = 'Арендодатель'


   

  