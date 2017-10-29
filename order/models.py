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
    total_price = models.DecimalField(max_digits=9, decimal_places=2, default=.0)
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
    quantity = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=9, decimal_places=2, default=.0)
    total_price = models.DecimalField(max_digits=9, decimal_places=2, default=.0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.product.name

    def save(self, *args, **kwargs):
        self.price_per_item = self.product.price
        self.total_price = self.quantity * self.price_per_item
        super(ProductInOrder, self).save(*args, **kwargs)
        all_products_in_order = ProductInOrder.objects.filter(order=self.order, is_active=True)

        order_total_price = 0
        for product_in_order in all_products_in_order:
            order_total_price += product_in_order.total_price

        self.order.total_price = order_total_price
        self.order.save(force_update=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
