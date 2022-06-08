from django.shortcuts import render, redirect
from .models import *
from .forms import prodform

# Create your views here.

def home(request):
    products=Product.objects.all()
    return render(request,'main.html',{'products':products})

def add_warehouse(request):
    if request.method=='POST':
        number=request.POST.get('number')
        new_warehouse=Warehouse(number=number)
        new_warehouse.save()
        return redirect('/')

    return render(request,'addwarehouse.html')

def add_category(request):
    if request.method=='POST':
        category=request.POST.get('category')
        new_category=Category(category=category)
        new_category.save()
        return redirect('/')
    return render(request,'addcategory.html')

def add_product(request):
    f = prodform(request.POST)
    if f.is_valid():
        f.save()
        return redirect('add_product')
    return render(request,'addproduct.html',{'f':f})

def stock(request):
    product=Product.objects.all().filter(stock__gt=0)
    return render(request,'stock.html',{'product':product})

def unstock(request):
    product=Product.objects.all().filter(stock__lte=0)
    return render(request,'unstock.html',{'product':product})

def warehouse(request):
    warehouse=Warehouse.objects.all()
    return render(request,'warehouse.html',{'warehouse':warehouse})

def products(request):
    products=Product.objects.all()
    return render(request,'products.html',{'products':products})
def ware_prod(request,id):
    products=Product.objects.filter(warehouse=id)
    count=Product.objects.filter(warehouse=id).count()
    total=250-count
    return render(request,'wareproducts.html',{'products':products,'total':total,'id':id})

