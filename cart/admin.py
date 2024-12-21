from django.contrib import admin
from .models import cart,cartDetails
class cartDetailsAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')
    list_filter = ('cart', 'product')
    search_fields = ('cart', 'product')
    ordering = ('cart','product')
# Register your models here.
admin.site.register(cart)
admin.site.register(cartDetails, cartDetailsAdmin)