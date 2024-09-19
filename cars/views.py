from django.shortcuts import render
from .models import Car
# Create your views here.

def index(request):
    objects = Car.objects.all()
    context={
        "obj":objects
    }
    return render(request,"index.html",context)