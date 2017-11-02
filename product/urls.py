from django.conf.urls import url

from product import views


urlpatterns = [
    url(r'^product/(?P<pk>[0-9]+)$', views.ProductDetail.as_view(), name='product_detail'),
]
