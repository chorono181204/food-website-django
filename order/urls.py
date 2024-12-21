
from django.urls import path
from .views import ViewOrder, ViewPlaceOrder, ViewOrderDetails

app_name = 'order'
urlpatterns=[
  path('order/', ViewOrder.as_view(), name='order'),
  path('api/placeorder/',ViewPlaceOrder.as_view(), name='placeorder'),
  path('orderdetails/<int:order_id>/', ViewOrderDetails.as_view(), name='orderdetails'),
]