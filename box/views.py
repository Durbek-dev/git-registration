from django.shortcuts import render
from .models import *
from django.views import generic
from .form import *

def home(request):
    connect = Carousel.objects.all()
    context = {
        "view": connect
    }
    return render(request, 'pages/home.html', context)

