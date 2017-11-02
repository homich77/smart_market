from django.views.generic import TemplateView
from django.shortcuts import render

from product.models import ProductImage


class HomeView(TemplateView):
    template_name = "landing/home.html"

    def get(self, request, *args, **kwargs):
        product_images = ProductImage.objects.filter(is_active=True, is_main=True)
        return render(request, self.template_name, {'product_images': product_images})
