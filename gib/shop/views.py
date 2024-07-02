from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.


def index(request):
    # product = Product.objects.all()
    # n = len(product)
    # noslides = n//4 + ceil((n / 4) + (n // 4))
    allprods=[]
    catprods= Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        noslides = n//4 + ceil((n / 4) + (n // 4))
        allprods.append([prod , range(1,noslides),noslides])
    # allprods = [[product , range(1,noslides) , noslides] , [product , range(1,noslides) , noslides]]
    params = {'allprods':allprods}
    return render(request, 'shop/index.html', params)

#1234
def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return render(request,'shop/contact.html')


def tracker(request):
    return render(request,'shop/tracker.html')


def search(request):
    return render(request,'shop/search.html')


def productview(request,id):
    #fetch the product using the id 
    return render(request,'shop/prodview.html')


def checkout(request):
    return render(request,'shop/checkout.html')
