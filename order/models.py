from django.db import models
from user.models import customer
from product.models import product
# Create your models here.
class order(models.Model):
    STATUS_CHOICES = [(0, 'Đã xác nhận'), (1, 'Đang giao hàng'), (2, 'Giao hàng thành công'), ]
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    address=models.CharField(max_length=250,default='')
    date=models.DateField(auto_now=True)
    total=models.IntegerField(default=0)
    status=models.IntegerField(default=0,choices=STATUS_CHOICES)
    note=models.CharField(max_length=250,default='')
    code=models.CharField(max_length=250,default='')
    phone=models.CharField(max_length=250,default='')
    def __str__(self):
        return self.code
class orderDetails(models.Model):
    order=models.ForeignKey(order, on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    total_price=models.IntegerField(default=0)
    def __str__(self):
        return self.order.code
    class Meta:
        verbose_name = 'Order Details'
        verbose_name_plural = 'Order Details'
