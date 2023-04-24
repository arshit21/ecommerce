from django.shortcuts import render
from products.models import product

def index(request):
    products = product.objects.order_by('-list_date')[:3]
    context = {
        'products': products
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request,'pages/about.html' )