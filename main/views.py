from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def product(request):
    return render(request, 'product.html')


def product_details(request):
    return render(request, 'product-details.html')


def cart(request):
    return render(request, 'cart.html')


def account(request):
    return render(request, 'account.html')
