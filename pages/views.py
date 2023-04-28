from django.shortcuts import render
from products.models import product
from products.choices import sport_choices, price_choices

def index(request):
    products = product.objects.order_by('-sales')[:3]
    context = {
        'sport_choices': sport_choices,
        'price_choices': price_choices,
        'products': products
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request,'pages/about.html' )