from django.db.models import Avg
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import Http404
# Create your views here.


def product_list(request):
    products = Product.objects.all().order_by('title')
    number_of_products = products.count()
    return render(request, 'product_module/product_list.html', context={
        'products': products,
        'number_of_products': number_of_products,
    })


def product_detail(request, slug):
    # try:
    #     product = Product.objects.get(id=product_id)
    # except:
    #     raise Http404
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product_module/product_detail.html', context={
        'product': product
    })
