from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import product

def index(request):

    products = product.objects.order_by('-list_date')
    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    context = {
        'products' : paged_products
    }
    return render(request, 'products/products.html', context)

def Product(request, product_id):
    Product = get_object_or_404(product, pk=product_id)
    context = {
        'product': Product
    }
    return render(request, 'products/product.html', context)

