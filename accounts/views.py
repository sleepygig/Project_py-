from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'accounts/dashboard.html')

def customer(request):
    return render(request,'accounts/customer.html')
    
def products(request):
    return render(request,'accounts/products.html')
    
    

# Create your views here.
