from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name = 'Pituchini'
    context = {'name': name}
    return render(request, 'bathhouse/index.html', context=context)