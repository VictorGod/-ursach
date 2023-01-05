from django.db import models


class Opening_Hours (models.Model):
  
    Monday=models.CharField(verbose_name="Понедельник",max_length=255)
    Tuesday=models.CharField(verbose_name="Вторник",max_length=255)
    Wednesday=models.CharField(verbose_name="Среда",max_length=255)
    Thursday=models.CharField(verbose_name="Четверг",max_length=255)
    Friday=models.CharField(verbose_name="Пятница",max_length=255)
    Saturday=models.CharField(verbose_name="Суббота",max_length=255)
    Sunday=models.CharField(verbose_name="Воскресенье",max_length=255)
 
def __str__(self):
        return self.Monday

class Meta:
        verbose_name = 'Время работы'
        verbose_name_plural = 'Время работы'

