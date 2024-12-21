from django.urls import path

from dashboard.views import ViewSalesChart, ViewTotal, ViewRevenueChart

app_name = 'dashboard'
urlpatterns = [
    path('api/saleschart/',ViewSalesChart.as_view(),name='saleschart'),
    path('api/total/',ViewTotal.as_view(),name='total'),
    path('api/revenuechart/',ViewRevenueChart.as_view(),name='revenuechart'),
]