import random
from datetime import datetime
from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.models import cart, cartDetails

from order.serializers import OrderSerializer
from product.models import category
from .models import orderDetails,order

class ViewOrder(View):
    def get(self, request):
        customer_cart=cart.objects.get(customer=request.user)
        cdts=cartDetails.objects.filter(cart=customer_cart)
        # danh muc
        categories = category.objects.all()
        context={"cdts":cdts,"customer_cart":customer_cart,'categories':categories}
        return render(request,'order/order.html',context)
class ViewPlaceOrder(APIView):
    def post(self, request):
        serializer=OrderSerializer(data=request.data)
        if serializer.is_valid():
            customer_cart = cart.objects.get(customer=request.user)
            name=serializer.validated_data['name']
            address=serializer.validated_data['address']
            phone=serializer.validated_data['phone']
            note=serializer.validated_data['note']
            order_code="ORD"+str(random.randint(1,99999))
            new_order=order.objects.create(customer=request.user,name=name,address=address,phone=phone,note=note,total=customer_cart.total,code=order_code)
            cdts=cartDetails.objects.filter(cart=customer_cart)
            for cdt in cdts:
               orderDetails.objects.create(order=new_order,product=cdt.product,quantity=cdt.quantity,total_price=cdt.total)
            cdts.delete()


            return Response({"status_order": True}, status=status.HTTP_200_OK)
class ViewOrderDetails(View):
    def get(self, request, order_id):
        od=order.objects.get(id=order_id)
        odt=orderDetails.objects.filter(order=od)
        # danh muc
        categories = category.objects.all()
        context={"od":od,"odt":odt,"categories":categories}
        return render(request,'order/orderdetails.html',context)