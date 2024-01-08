from django.db import models

# Create your models here.

class People(models.Model):
    name = models.CharField(max_length=100, help_text='Введите имя!', verbose_name='Имя!')
    description = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(verbose_name='Дата рождения!')
    photo = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name



