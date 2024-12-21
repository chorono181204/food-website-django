from django.contrib import admin
from django.utils.html import format_html

from .models import product, category
class productAdmin(admin.ModelAdmin):
    list_display = ('name','category', 'price', 'isNew' ,'isSale','discount','image_tag')
    list_filter = ('category', 'isNew', 'price')
    search_fields = ('name', 'category__name')
    ordering = ('category', 'price', 'name')
    readonly_fields = ('image_tag',)
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.image.url))
        return "-"
        image_tag.short_description = 'Image'
class categoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_product')
    search_fields = ('name',)
    def total_product(self, obj):
        products=product.objects.filter(category=obj)
        return products.count()
# Register your models here.
admin.site.register(product, productAdmin)
admin.site.register(category, categoryAdmin)
