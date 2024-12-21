from django.contrib import admin
from .models import customer
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_code','email', 'name', 'is_authenticated','date_joined')
    list_filter = ('is_authenticated', 'date_joined')
    search_fields = ('customer_code','email', 'name','date_joined')
    ordering = ('date_joined', 'customer_code', 'email')
admin.site.register(customer, CustomerAdmin)