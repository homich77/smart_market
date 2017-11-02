from django.views.generic import TemplateView
from django.shortcuts import render

from product.models import ProductImage


class HomeView(TemplateView):
    template_name = "landing/home.html"

    def get(self, request, *args, **kwargs):
        product_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
        product_images_phone = product_images.filter(product__category=1)
        product_images_laptop = product_images.filter(product__category=2)
        context = {
            'product_images': product_images,
            'product_images_phone': product_images_phone,
            'product_images_laptop': product_images_laptop
        }
        return render(request, self.template_name, context=context)
