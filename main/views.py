from django.shortcuts import render
from .models import *

def home(request):
    # content = {
    #     "softwares" : softwares.objects.all()
    # }
    # print(softwares.objects.all().values("photo"))
    return render(request, 'index.html')

def categories(request):
    return render(request, 'categories.html')

def product_details(request):
    return render(request, 'product-details.html')

def contact(request):
    return render(request, 'contact.html')