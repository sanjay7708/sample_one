from django.shortcuts import render,redirect
from . models import Product
from . froms import ProductForm
# Create your views here.

def home(request):
    obj=Product.objects.all()
    return render(request,'home.html',{'data':obj})
def insert(request):
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=ProductForm()
    return render(request,'insert.html',{'form':form})
