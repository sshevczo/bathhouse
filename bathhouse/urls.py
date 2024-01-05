from django.urls import path
from .views import index

app_name = 'bathhouse'

urlpatterns = [
    path('', index, name='index')
]
