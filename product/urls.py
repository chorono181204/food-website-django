from django.urls import path
from . import views
from .views import ViewListProduct, ViewProductByCategory, ViewProductBySearh, ViewProductDetails

app_name='product'
urlpatterns=[
path('', ViewListProduct.as_view(), name='listproduct'),
path('productsbycategory/', ViewProductByCategory.as_view(), name='listproductbycate'),
path('productsbysearch/', ViewProductBySearh.as_view(), name='listproductbysearch'),
path('productdetails/<int:product_id>', ViewProductDetails.as_view(), name='productdetails'),
]