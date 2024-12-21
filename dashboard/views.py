from datetime import datetime
from lib2to3.fixes.fix_input import context
from time import daylight

from django.db.models import Sum
from django.db.models.functions import TruncDay
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from order.models import orderDetails, order
from product.models import category, product
from user.models import customer


# Create your views here.
class ViewSalesChart(APIView):
    def get(self, request):
        month=datetime.today().month
        data=orderDetails.objects.filter(order__date__month=month).values('product__category__name').annotate(total_sold=Sum('quantity')).order_by('-total_sold')
        return Response(data)
class ViewTotal(APIView):
    def get(self, request):
        month = datetime.today().month
        data=order.objects.filter(date__month=month).aggregate(revenue=Sum('total'))
        data['total_orders']=order.objects.filter(date__month=month).count()
        data['new_users']=customer.objects.filter(date_joined__month=month).count()
        data.update(orderDetails.objects.filter(order__date__month=month).aggregate(total_sales=Sum('quantity')))
        return Response(data)
class ViewRevenueChart(APIView):
    def get(self, request):
        now = datetime.now()
        start_date = datetime(now.year, now.month, 1)
        end_date = datetime(now.year, now.month + 1, 1) if now.month < 12 else datetime(now.year + 1, 1, 1)
        data=order.objects.filter(date__gte=start_date, date__lte=end_date).annotate(day=TruncDay('date')).values('day').annotate(total_revenue=Sum('total')).order_by('day')
        return Response(data)