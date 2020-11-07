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
    context = {'product': products, 'exclusive': exclusive, 'offer': offer, 'category':category}
    return render(request, 'index.html', context)


def product(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product.html', context)


def product_details(request):
    return render(request, 'product-details.html')


def cart(request):
    return render(request, 'cart.html')


def account(request):
    return render(request, 'account.html')
