from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced

# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
    def get(self, request):
        trending = Product.objects.filter(category='T')
        
        latest_fashion = Product.objects.filter(category='MS')|Product.objects.filter(category='MJ')
        jeans_men = Product.objects.filter(category='MJ')
        tops_women = Product.objects.filter(category='WT')
        active_wears_women = Product.objects.filter(category='WA')
        return render(request, 'app/home.html', {'trending':trending, 'latest_fashion':latest_fashion, 'tops_women':tops_women, 'active_wears_women':active_wears_women})

# def product_detail(request):
#  return render(request, 'app/productdetail.html')

class ProdutDetailView(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', {'product': product})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
