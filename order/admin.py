from django.contrib import admin
from .models import orderDetails, order

# Register your models here.
class orderModelAdmin(admin.ModelAdmin):
    list_display = ('code','name' ,'date', 'total','status')
    list_filter = ('code', 'status','date')
    search_fields = ('name','code','address')
    ordering = ('code','status','code')
class orderDetailsModelAdmin(admin.ModelAdmin):
    list_display = ('order', 'product','quantity')
    list_filter = ('order', 'product', 'quantity')
    search_fields = ('order', 'product')
    ordering = ('order', 'product')
admin.site.register(order,orderModelAdmin)
admin.site.register(orderDetails,orderDetailsModelAdmin)