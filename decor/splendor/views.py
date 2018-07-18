from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'index.html')

def shop(request):
    return render(request, 'shop.html')

def services(request):
    return render(request, 'services.html')

def cart(request):
    return render(request,'cart.html')

def product(request):
    return render(request, 'product-details.html')

def fourowfour(request):
    return render(request, '404.html')

def checkout(request):
    return render(request, 'checkout.html')

