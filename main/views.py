from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.models import auth
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.


def index(request):
    products = Product.objects.all()
    category = Category.objects.all()
    exclusive = Exclusive.objects.all()
    offer = Offer.objects.all()
    context = {
        'product': products,
        'exclusive': exclusive,
        'offer': offer,
        'category': category
    }
    return render(request, 'index.html', context)


def product(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product.html', context)


def product_details(request, pk=id):
    prod = Product.objects.get(id=pk)

    context = {'prod': prod}
    return render(request, 'product-details.html', context)


def add_cart_item(request):
    if request.method == 'POST':
        prodid = request.POST['prodid']
        qty = request.POST['qty']
        size = request.POST['size']
        item = Product.objects.get(id=prodid)
        print(request.user)
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,
                                                     
                                                     complete=False)
         
                                           
        orderitem = OrderItem(product=item, order=order, value=qty,size=size)
        orderitem.save()
        return JsonResponse({'message': 'Success'})


def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,
                                                     complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_item': 0, 'get_cart_total': 0}

    context = {'items': items, 'order': order}
    return render(request, 'cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,
                                                     complete=False)
        items = order.orderitem_set.all()

    else:
        items = []
        order = {'get_cart_item': 0, 'get_cart_total': 0}
    context = {'items': items, 'order': order}
    return render(request, 'checkout.html', context)


def payment(request):
    return HttpResponse("will be added soon")


# Login
def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=name,
                                 useremail=email,
                                 password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,
                          'invalid info please make sure username & password')
            return redirect('/signup')
    else:
        return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('/')


# signup
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        print(name, email, password)
        user = User.objects.create_user(username=name,
                                        email=email,
                                        password=password)
        customer = Customer(user=user, name=name, email=email)
        customer.save()
        return redirect('login')
    # return render(request, 'account.html')
