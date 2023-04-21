from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm, CustomerPofileForm
from django.contrib import messages 


class ProductView(View):
    def get(self, request):
        trending = Product.objects.filter(category='T')
        latest_fashion = Product.objects.filter(category='WT')|Product.objects.filter(category='WJ')
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


def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html', {'add':add, 'active':'btn-primary'})

def orders(request):
 return render(request, 'app/orders.html')


def mshirts(request,data=None):
    if data == None:
        mshirts = Product.objects.filter(category='MS')
    elif data == 'Levis' or data == 'Raymond':
        mshirts = Product.objects.filter(category='MS').filter(brand=data)
    return render(request, 'app/mshirts.html',{'mshirts':mshirts})

def mhoodjack(request,data=None):
    if data == None:
        mhoodjack = Product.objects.filter(category='MHJ')
    elif data == 'Levis' or data == 'Raymond':
        mhoodjack = Product.objects.filter(category='MHJ').filter(brand=data)
    return render(request, 'app/mhoodjack.html',{'mhoodjack':mhoodjack})

def mjeans(request,data=None):
    if data == None:
        mjeans = Product.objects.filter(category='MJ')
    elif data == 'Levis' or data == 'Raymond':
        mjeans = Product.objects.filter(category='MJ').filter(brand=data)
    return render(request, 'app/mjeans.html',{'mjeans':mjeans})

def mtrouser(request,data=None):
    if data == None:
        mtrouser = Product.objects.filter(category='MT')
    elif data == 'Levis' or data == 'Raymond':
        mtrouser = Product.objects.filter(category='MT').filter(brand=data)
    return render(request, 'app/mtrouser.html',{'mtrouser':mtrouser})

def mactivewear(request,data=None):
    if data == None:
        mactivewear = Product.objects.filter(category='MA')
    elif data == 'Levis' or data == 'Raymond':
        mactivewear = Product.objects.filter(category='MA').filter(brand=data)
    return render(request, 'app/mactivewear.html',{'mactivewear':mactivewear})

def wdress(request,data=None):
    if data == None:
        wdress = Product.objects.filter(category='WD')
    elif data == 'Levis' or data == 'Raymond':
        wdress = Product.objects.filter(category='WD').filter(brand=data)
    return render(request, 'app/wdress.html',{'wdress':wdress})

def wtops(request,data=None):
    if data == None:
        wtops = Product.objects.filter(category='WT')
    elif data == 'Levis' or data == 'Raymond':
        wtops = Product.objects.filter(category='WT').filter(brand=data)
    return render(request, 'app/wtops.html',{'wtops':wtops})

def wjeans(request,data=None):
    if data == None:
        wjeans = Product.objects.filter(category='WJ')
    elif data == 'Levis' or data == 'Raymond':
        wjeans = Product.objects.filter(category='WJ').filter(brand=data)
    return render(request, 'app/wjeans.html',{'wjeans':wjeans})

def wskirts(request,data=None):
    if data == None:
        wskirts = Product.objects.filter(category='WS')
    elif data == 'Levis' or data == 'Raymond':
        wskirts = Product.objects.filter(category='WS').filter(brand=data)
    return render(request, 'app/wskirts.html',{'wskirts':wskirts})

def wactivewear(request,data=None):
    if data == None:
        wactivewear = Product.objects.filter(category='WA')
    elif data == 'Levis' or data == 'Raymond':
        wactivewear = Product.objects.filter(category='WA').filter(brand=data)
    return render(request, 'app/wactivewear.html',{'wactivewear':wactivewear})

def girls(request,data=None):
    if data == None:
        girls = Product.objects.filter(category='KB')
    elif data == 'Levis' or data == 'Raymond':
        girls = Product.objects.filter(category='KB').filter(brand=data)
    return render(request, 'app/girls.html',{'girls':girls})

def boys(request,data=None):
    if data == None:
        boys = Product.objects.filter(category='KG')
    elif data == 'Levis' or data == 'Raymond':
        boys = Product.objects.filter(category='KG').filter(brand=data)
    return render(request, 'app/boys.html',{'boys':boys})

class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',{'form':form})
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Registered Successfully!!!')
            form.save()
        return render(request, 'app/customerregistration.html',{'form':form})
        
def checkout(request):
 return render(request, 'app/checkout.html')


class ProfileView(View):
    def get(self,request):
        form = CustomerPofileForm()
        return render(request, 'app/profile.html',{'form':form, 'active':'btn-primary'})
    
    def post(self,request):
        form = CustomerPofileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user = usr, name=name, locality=locality, city=city, state=state, zipcode=zipcode) 
            reg.save()
            messages.success(request, 'Congratulations!! Profile Updated Successgully')
        return render(request, 'app/profile.html',{'form':form, 'active':'btn-primary'})

 