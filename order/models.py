from django.db import models

from product.models import Product


class Status(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"


class Order(models.Model):
    price_total_amount = models.DecimalField(max_digits=9, decimal_places=2, default=.0)
    status = models.ForeignKey(Status)
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    comment = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Order %s %s" % (self.customer_name, self.status.name)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    quantity = models.ImageField(default=1)
    price_per_item = models.DecimalField(max_digits=9, decimal_places=2, default=.0)
    price_total = models.DecimalField(max_digits=9, decimal_places=2, default=.0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
