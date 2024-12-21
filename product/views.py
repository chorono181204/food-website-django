from contextlib import nullcontext
from lib2to3.fixes.fix_input import context
from math import ceil
from msilib.schema import tables

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from order.models import orderDetails
from product.models import product, category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, Sum


# Create your views here.
class ViewListProduct(View):
    def get(self, request):
        #danh muc
        categories = category.objects.all()
        #phan trang product
        listProduct = product.objects.all()
        paginator = Paginator(listProduct, 9)
        pageNumber = request.GET.get('page')
        num=ceil(listProduct.count()/9)
        pages=[]
        saleProduct=product.objects.filter(isSale=True)
        for i in range(1, num+1):
            pages.append(i)
        try:
            products = paginator.page(pageNumber)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        login=True
        if not request.user.is_authenticated:
            login=False
        context={'products':products,'categories':categories,'listProduct':listProduct,'pages':pages,'login':login,'saleProduct':saleProduct}
        return render(request,'product/listproduct.html',context)
class ViewProductByCategory(View):
    def get(self, request):
        # danh muc
        categories = category.objects.all()
        categoryId=request.GET.get('id')
        if categoryId:
            Category = category.objects.get(id=categoryId)
            listProductByCate = product.objects.filter(category=Category)
        else:
            Category = nullcontext
            listProductByCate = product.objects.all()
        listProduct = product.objects.all()
        paginator = Paginator(listProductByCate, 12)
        pageNumber = request.GET.get('page')
        num = ceil(listProductByCate.count() / 12)
        pages = []
        request.session['total'] = 150
        for i in range(1, num + 1):
            pages.append(i)
        try:
            products = paginator.page(pageNumber)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        login = True
        if not request.user.is_authenticated:
            login = False
        context = {'products': products, 'categories': categories,
                   'pages': pages,'listProduct':listProduct,'Category':Category,'listProductByCate':listProductByCate,'login':login}
        return render(request, 'product/listproductbycate.html', context)
class ViewProductBySearh(View):
    def get(self, request):
        keyword=request.GET.get('keyword')
        # danh muc
        categories = category.objects.all()
        if keyword:
            keywords = keyword.strip().split(' ')
            q_objects = Q()
            for key in keywords:
                q_objects |= Q(name__icontains=key) | Q(details__icontains=keyword)
            listProductBySearch = product.objects.filter(q_objects)
        else:
            listProductBySearch = product.objects.all()
        listProduct = product.objects.all()
        paginator = Paginator(listProductBySearch, 12)
        pageNumber = request.GET.get('page')
        num = ceil(listProductBySearch.count() / 12)
        pages = []
        for i in range(1, num + 1):
            pages.append(i)
        try:
            products = paginator.page(pageNumber)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        login = True
        if not request.user.is_authenticated:
            login = False
        context = {'products': products, 'categories': categories,
                   'pages': pages, 'listProduct': listProduct,
                   'listProductByCate': listProductBySearch,'keyword':keyword,'login':login}
        return render(request, 'product/listproductbysearch.html', context)
class ViewProductDetails(View):
    def get(self, request,product_id):
        # danh muc
        categories = category.objects.all()
        #sanphan
        productById=product.objects.get(id=product_id)
        categoryByProduct = productById.category
        relatedProduct=product.objects.filter(category=categoryByProduct)
        odts=orderDetails.objects.filter(product=productById)
        sold=0
        for odt in odts:
            sold+=odt.quantity
        login = True
        if not request.user.is_authenticated:
            login = False
        context={'categories':categories,'productById':productById,'categoryByProduct':categoryByProduct,'relatedProduct':relatedProduct,'login':login,'sold':sold}
        return render(request,'product/productdetails.html',context)