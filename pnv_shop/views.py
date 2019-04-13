from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'pnv_shop/index.html')

def about(request):
    return HttpResponse("about")

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