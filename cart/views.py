from django.shortcuts import render, redirect
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import product, category
from user.models import customer
from .models import cart, cartDetails
from .serializers import CartDetailsSerializer, DeleteCartDetailsSerializer, AddToCartDetailsSerializer


# Create your views here.
class ViewCart(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/login')
        user=request.user
        #danh muc
        categories = category.objects.all()
        c=cart.objects.get(customer=user)
        cdts=cartDetails.objects.filter(cart=c)
        context = {'cdts': cdts,'categories':categories}
        return render(request,'cart/cart.html',context)
class ViewUpdateCart(APIView):
    def put(self, request):
        serializer = CartDetailsSerializer(data=request.data)
        if serializer.is_valid():
           ids=serializer.validated_data.get('ids')
           quantities=serializer.validated_data.get('quantities')
           for i in range(len(ids)):
               cartdetails=cartDetails.objects.get(id=ids[i])
               if quantities[i]!=0:
                    cartdetails.quantity=quantities[i]
                    cartdetails.save()
               else:
                   cartdetails.delete()
           return Response({"status":True},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ViewDeleteCart(APIView):
    def delete(self, request):
        serializer = DeleteCartDetailsSerializer(data=request.data)
        if serializer.is_valid():
            id=serializer.validated_data.get('id')
            cartdetails=cartDetails.objects.get(id=id)
            cartdetails.delete()
            return Response({"status_delete":True},status=status.HTTP_200_OK)
class ViewAddToCart(APIView):
    def post(self, request):
        serializer = AddToCartDetailsSerializer(data=request.data)
        if serializer.is_valid():
            customer_cart=cart.objects.get(customer=request.user)
            cdts=cartDetails.objects.filter(cart=customer_cart)
            id=serializer.validated_data.get('id')
            quantity=serializer.validated_data.get('quantity')
            p=product.objects.get(id=id)
            if quantity!=0:
                for item in cdts:
                    if item.product==p:
                        item.quantity=item.quantity+quantity
                        item.save()
                        return Response({"status_add": True}, status=status.HTTP_200_OK)
                cartDetails.objects.create(cart=customer_cart, product=p, quantity=quantity)
                return Response({"status_add": True}, status=status.HTTP_200_OK)