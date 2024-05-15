from django.db.models import Avg
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import Product
from django.http import Http404

# Create your views here.


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        base_query = super(ProductListView, self).get_queryset()
        data = base_query.filter(is_active=True)
        return data


class ProductDetailView(TemplateView):
    template_name = 'product_module/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data()
        slug = kwargs['slug']
        product = get_object_or_404(Product, slug=slug)
        context['product'] = product
        return context


# class ProductListView(TemplateView):
#     template_name = 'product_module/product_list.html'
#
#     def get_context_data(self, **kwargs):
#         products = Product.objects.all().order_by('title')[:5]
#         context = super(ProductListView, self).get_context_data()
#         context['products'] = products
#         return context


# def product_list(request):
#     products = Product.objects.all().order_by('title')[:5]
#     return render(request, 'product_module/product_list.html', context={
#         'products': products,
#     })


# def product_detail(request, slug):
#     # try:
#     #     product = Product.objects.get(id=product_id)
#     # except:
#     #     raise Http404
#     product = get_object_or_404(Product, slug=slug)
#     return render(request, 'product_module/product_detail.html', context={
#         'product': product
#     })
