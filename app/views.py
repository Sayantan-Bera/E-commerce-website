from django.shortcuts import render , redirect
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages 
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ProductView(View):
    def get(self, request):
        totalitem = 0
        trending = Product.objects.filter(category='T')
        latest_fashion = Product.objects.filter(category='WT')|Product.objects.filter(category='WJ')
        kids = Product.objects.filter(category="KB")|Product.objects.filter(category='KG')
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
        return render(request, 'app/home.html', {'trending':trending, 'latest_fashion':latest_fashion, 'kids':kids, 'totalitem':totalitem})

# def product_detail(request):
#  return render(request, 'app/productdetail.html')

class ProdutDetailView(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        item_incart = False
        totalitem = 0
        if request.user.is_authenticated:
            item_incart = Cart.objects.filter(Q(product=product.id) & Q(user = request.user)).exists()
            totalitem = len(Cart.objects.filter(user=request.user))
            
        return render(request, 'app/productdetail.html', {'product': product , 'item_incart': item_incart, 'totalitem':totalitem})

@login_required
def add_to_cart(request):
    try:
        if request.user.is_authenticated:
            user = request.user
            product_id = request.GET.get('prod_id')
            product = Product.objects.get(id=product_id)
            Cart(user=user,product=product).save()      
    except Product.DoesNotExist:
        product = None

    return redirect('/cart')

@login_required
def show_cart(request):
    totalitem = 0
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        totalitem = len(Cart.objects.filter(user=request.user))
        amount = 0
        shipping_amount = 70
        totalamount = 0
        cart_product = [p for p in Cart.objects.all() if p.user==user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity* p.product.discounted_price)
                amount += tempamount
                totalamount = amount + shipping_amount
            return render(request, 'app/addtocart.html', {'carts':cart , 'totalamount': totalamount, 'amount':amount, 'totalitem':totalitem})
        else:
            return render(request, 'app/emptycart.html', {'totalitem':totalitem})

@login_required
def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product = prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0
        shipping_amount = 70
        cart_product = [p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
            tempamount = (p.quantity* p.product.discounted_price)
            amount += tempamount

        data = {
            'quantity' : c.quantity,
            'amount' : amount,
            'totalamount': amount + shipping_amount
        }
        return JsonResponse(data)

@login_required
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product = prod_id) & Q(user=request.user))
        if (c.quantity == 1):
            c.quantity=1
        else:
            c.quantity -= 1
        c.save()
        amount = 0
        shipping_amount = 70
        cart_product = [p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
            tempamount = (p.quantity* p.product.discounted_price)
            amount += tempamount

        data = {
            'quantity' : c.quantity,
            'amount' : amount,
            'totalamount': amount + shipping_amount
        }
        return JsonResponse(data)

@login_required
def remove_cart(request):
    totalitem = 0
    if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product = prod_id) & Q(user=request.user))
        c.delete()
        amount = 0
        shipping_amount = 70
        cart_product = [p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
            tempamount = (p.quantity* p.product.discounted_price)
            amount += tempamount

        data = {
            'amount' : amount,
            'totalamount': amount + shipping_amount
        }
        return JsonResponse(data)

@login_required
def buy_now(request):
 return render(request, 'app/buynow.html')

@login_required
def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html', {'add':add, 'active':'btn-primary'})

def orders(request):
 return render(request, 'app/orders.html')


def mshirts(request,data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        mshirts = Product.objects.filter(category='MS')
    elif data == 'below':
        mshirts = Product.objects.filter(category='MS').filter(discounted_price__lt=3600)
    elif data == 'above':
        mshirts = Product.objects.filter(category='MS').filter(discounted_price__gt=3600)
    return render(request, 'app/mshirts.html',{'mshirts':mshirts, 'totalitem':totalitem})

def mhoodjack(request,data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        mhoodjack = Product.objects.filter(category='MHJ')
    elif data == 'below':
        mhoodjack = Product.objects.filter(category='MHJ').filter(discounted_price__lt=4500)
    elif data == 'above':
        mhoodjack = Product.objects.filter(category='MHJ').filter(discounted_price__gt=4500)
    return render(request, 'app/mhoodjack.html',{'mhoodjack':mhoodjack, 'totalitem':totalitem})

def mjeans(request,data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        mjeans = Product.objects.filter(category='MJ')
    elif data == 'below':
        mjeans = Product.objects.filter(category='MJ').filter(discounted_price__lt=3000)
    elif data == 'above':
        mjeans = Product.objects.filter(category='MJ').filter(discounted_price__gt=3000)
    return render(request, 'app/mjeans.html',{'mjeans':mjeans, 'totalitem':totalitem})

def mtrouser(request,data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        mtrouser = Product.objects.filter(category='MT')
    elif data == 'below':
        mtrouser = Product.objects.filter(category='MT').filter(discounted_price__lt=3000)
    elif data == 'above':
        mtrouser = Product.objects.filter(category='MT').filter(discounted_price__gt=3000)
    return render(request, 'app/mtrouser.html',{'mtrouser':mtrouser, 'totalitem':totalitem})

def mactivewear(request,data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        mactivewear = Product.objects.filter(category='MA')
    elif data == 'below':
        mactivewear = Product.objects.filter(category='MA').filter(discounted_price__lt=3000)
    elif data == 'above':
        mactivewear = Product.objects.filter(category='MA').filter(discounted_price__gt=3000)
    return render(request, 'app/mactivewear.html',{'mactivewear':mactivewear, 'totalitem':totalitem})

def wdress(request,data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        wdress = Product.objects.filter(category='WD')
    elif data == 'below':
        wdress = Product.objects.filter(category='WD').filter(discounted_price__lt=3000)
    elif data == 'above':
        wdress = Product.objects.filter(category='WD').filter(discounted_price__gt=3000)
    return render(request, 'app/wdress.html',{'wdress':wdress, 'totalitem':totalitem})

def wtops(request,data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        wtops = Product.objects.filter(category='WT')
    elif data == 'below':
        wtops = Product.objects.filter(category='WT').filter(discounted_price__lt=3000)
    elif data == 'above':
        wtops = Product.objects.filter(category='WT').filter(discounted_price__gt=3000)
    return render(request, 'app/wtops.html',{'wtops':wtops, 'totalitem':totalitem})

def wjeans(request,data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        wjeans = Product.objects.filter(category='WJ')
    elif data == 'below':
        wjeans = Product.objects.filter(category='WJ').filter(discounted_price__lt=3000)
    elif data == 'above':
        wjeans = Product.objects.filter(category='WJ').filter(discounted_price__gt=3000)
    return render(request, 'app/wjeans.html',{'wjeans':wjeans, 'totalitem':totalitem})

def wskirts(request,data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        wskirts = Product.objects.filter(category='WS')
    elif data == 'below':
        wskirts = Product.objects.filter(category='WS').filter(discounted_price__lt=3000)
    elif data == 'above':
        wskirts = Product.objects.filter(category='WS').filter(discounted_price__gt=3000)
    return render(request, 'app/wskirts.html',{'wskirts':wskirts, 'totalitem':totalitem})

def wactivewear(request,data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        wactivewear = Product.objects.filter(category='WA')
    elif data == 'below':
        wactivewear = Product.objects.filter(category='WA').filter(discounted_price__lt=3000)
    elif data == 'above':
        wactivewear = Product.objects.filter(category='WA').filter(discounted_price__gt=3000)
    return render(request, 'app/wactivewear.html',{'wactivewear':wactivewear, 'totalitem':totalitem})

def girls(request,data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        girls = Product.objects.filter(category='KG')
    elif data == 'below':
        girls = Product.objects.filter(category='KG').filter(discounted_price__lt=3000)
    elif data == 'above':
        girls = Product.objects.filter(category='KG').filter(discounted_price__gt=3000)
    return render(request, 'app/girls.html',{'girls':girls, 'totalitem':totalitem})

def boys(request,data=None):
    totalitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
    if data == None:
        boys = Product.objects.filter(category='KB')
    elif data == 'below':
        boys = Product.objects.filter(category='KB').filter(discounted_price__lt=3000)
    elif data == 'above':
        boys = Product.objects.filter(category='KB').filter(discounted_price__gt=3000)
    return render(request, 'app/boys.html',{'boys':boys, 'totalitem':totalitem})

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

@login_required      
def checkout(request):
 return render(request, 'app/checkout.html')

@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html',{'form':form, 'active':'btn-primary'})
    
    def post(self,request):
        form = CustomerProfileForm(request.POST)
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

 