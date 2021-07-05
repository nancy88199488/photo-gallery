from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from .models import Image,Location

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to my gallery')

def photos(request):
    images = Image.objects.all()
    location = Location.objects.all()
    return render(request, 'photos.html',{'images':images,'location':location})

