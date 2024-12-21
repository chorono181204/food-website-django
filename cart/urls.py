
from django.urls import path
from .views import ViewCart, ViewUpdateCart, ViewDeleteCart, ViewAddToCart

app_name = 'cart'
urlpatterns=[
   path('cart/', ViewCart.as_view(), name='cart'),
   path('api/updatecart/', ViewUpdateCart.as_view(), name='updatecart'),
   path('api/deletecart/', ViewDeleteCart.as_view(), name='deletecart'),
   path('api/addtocart/',ViewAddToCart.as_view(), name='addtocart'),
]