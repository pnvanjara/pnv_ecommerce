from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    print(products)
    params = {}
    return render(request,'pnv_shop/index.html',params)

def about(request):
    return render(request,'pnv_shop/about.html')

def contact(request):
    return HttpResponse("contact")

def tracker(request):
    return HttpResponse("tracker")

def productview(request):
    return HttpResponse("product view")

def checkout(request):
    return HttpResponse("checkout")

def search(request):
    return HttpResponse("search")