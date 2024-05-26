from django.db.models import Avg, Count
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, View
from .models import Product, ProductCategory, ProductBrand
from django.http import Http404, HttpRequest


# Create your views here.


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'
    ordering = ['price']
    paginate_by = 6

    def get_queryset(self):
        query = super(ProductListView, self).get_queryset()
        category_name = self.kwargs.get('cat')
        brand_name = self.kwargs.get('brand')

        if brand_name is not None:
            query = query.filter(brand__url_title__iexact=brand_name)

        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)

        return query


class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_product = self.object
        request = self.request
        favorite_product_id = request.session.get('product_favorite')
        context['is_favorite'] = favorite_product_id == str(loaded_product.id)
        return context


class AddProductFavorite(View):
    def post(self, request):
        product_id = request.POST['product_id']
        product = Product.objects.get(pk=product_id)
        request.session["product_favorite"] = product_id
        return redirect(product.get_absolute_url())


def product_categories_component(request: HttpRequest):
    product_categories = ProductCategory.objects.filter(is_active=True, is_delete=False).order_by('title')
    context = {
        'categories': product_categories
    }
    return render(request, 'product_module/components/product_categories_component.html', context)


def product_brands_component(request: HttpRequest):
    product_brands = ProductBrand.objects.annotate(product_count=Count('product')).filter(is_active=True).order_by(
        'title')
    context = {
        'brands': product_brands
    }
    return render(request, 'product_module/components/product_brand_component.html', context)

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
