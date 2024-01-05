from django.db import models

# Create your models here.

class People(models.Model):
    name = models.CharField(max_length=100, help_text='Введите имя!', verbose_name='Имя!')
    description = models.TextField(null=True, blank=True)