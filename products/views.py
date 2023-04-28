from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import product
from .choices import sport_choices, price_choices
from orders.choices import units_choices
from django.contrib import messages

def index(request):

    products = product.objects.order_by('-sales')
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    context = {
        'products' : paged_products
    }
    return render(request, 'products/products.html', context)

def Product(request, product_id):
    Product = get_object_or_404(product, pk=product_id)
    context = {
        'product': Product,
        'units_choices': units_choices
    }
    return render(request, 'products/product.html', context)

def search(request):
    queryset_list = product.objects.all()
    if 'sport' in request.GET:
        sport = request.GET['sport']
        if sport:
            queryset_list = queryset_list.filter(sport__iexact=sport)
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)
    context = {
        'sport_choices': sport_choices,
        'price_choices': price_choices,
        'products': queryset_list,
        'values': request.GET
    }
    return render(request, 'products/search.html', context)

def delete_product(request, product_id):
    Product = get_object_or_404(product, pk=product_id)
    Product.delete()
    messages.success(request, 'The Product has been deleted')
    return redirect('vendor_dashboard')