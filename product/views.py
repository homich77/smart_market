from django.views.generic.detail import DetailView

from .models import Product


class ProductDetail(DetailView):
    model = Product
    template_name = 'product/product_detail.html'
