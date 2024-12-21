from django.db import models
from product.models import product
from user.models import customer
# Create your models here.
class cart(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    @property
    def total(self):
        total = 0
        cdts=cartDetails.objects.filter(cart=self)
        for cdt in cdts:
            total += cdt.total
        return total
    def __str__(self):
        return str(self.customer)
class cartDetails(models.Model):
    cart = models.ForeignKey(cart, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return str(self.cart)
    @property
    def total(self):
        return self.product.afterDiscount*self.quantity
    class Meta:
        verbose_name = 'Cart Details'
        verbose_name_plural = 'Cart Details'