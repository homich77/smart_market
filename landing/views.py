from django.views.generic import TemplateView
from django.shortcuts import render

from product.models import ProductImage


class HomeView(TemplateView):
    template_name = "landing/home.html"

    def get(self, request, *args, **kwargs):
        products = ProductImage.objects.filter(is_active=True)
        return render(request, self.template_name, {'products': products})
