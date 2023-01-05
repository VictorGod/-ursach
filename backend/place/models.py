from django.db import models
from opening_hours.models import Opening_Hours

class Place (models.Model):
    address=models.CharField(verbose_name="адресс",max_length=255)
    entrance_number=models.CharField(verbose_name="№ Входа",max_length=255)
    floor=models.CharField(verbose_name="Этаж",max_length=255)
    table=models.CharField(verbose_name="Стол",max_length=255)
    opening_hours = models.ManyToManyField(to =Opening_Hours, related_name="Place" ) 
    square=models.CharField(verbose_name="Площадь",max_length=255)
    price=models.CharField(verbose_name="Цена",max_length=255)
    undeground=models.CharField(verbose_name="Метро",max_length=255)
    photo=models.ImageField(verbose_name="фото",upload_to="users/photos")
    bio =models.TextField(verbose_name="описание рабочего места")
def __str__(self):
        return self.work_address

class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Место' 


   
