from datetime import timezone, datetime
from lib2to3.fixes.fix_input import context
import random

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.core.serializers import serialize
from django.db.models.functions import Random
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from cart.models import cart
from order.models import order
from product.models import category,product
from user.forms import LoginForm, RegisterForm
from .forms import LoginForm
from .models import customer
from .serializers import CheckEmailSerializer, SignUpSerializer, ForgotPasswordSerializer,ChangePasswordSerializer
from HealthyFood import settings
from django.utils.encoding import force_str
# Create your views here.
class ViewLogin(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'user/loginandsignup.html')
    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        try :
            cus=customer.objects.get(email=email, password=password)
            if cus.is_authenticated:
                login(request,cus)
                return redirect('/')
            else:
                return render(request, 'user/loginandsignup.html', {'messagesauth': True,'id':cus.id})
        except:
            return render(request, 'user/loginandsignup.html',{'messageslogin':True,'email':email,'password':password})
        return render(request, 'user/loginandsignup.html')

#check email
class CheckEmail(APIView):
    def post(self, request):
        serializer = CheckEmailSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            if customer.objects.filter(email=email).exists():
                user = customer.objects.get(email=email)
                return Response({"exists": True,"id":user.id})
            else:
                return Response({"exists": False})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#signup


class SignUp(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            name = serializer.validated_data['name']
            code="CUS"+str(random.randint(1,99999))
            cus=customer.objects.create(email=email, password=password, name=name, is_active=True,last_login=datetime.now(),customer_code=code)
            customer_cart=cart.objects.create(customer=cus)
            return Response({"status": True,'id':cus.id})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#verify
class VerifyEmail(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        user_id=request.GET.get('id')
        user=customer.objects.get(id=user_id)
        if user.is_authenticated:
            return render(request, 'user/verifyemail.html',{'verified':True})
        else:
            current_site = get_current_site(request)
            mail_subject = 'Kích hoạt tài khoản của bạn.'
            message = render_to_string('email/verify.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email=user.email
            send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [to_email])

        return render(request, 'user/verifyemail.html')
class ActiveAccount(View):
    def get(self, request,uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = customer.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, customer.DoesNotExist):
            user = None
        if user is not None and default_token_generator.check_token(user, token):
            user.is_authenticated = True
            user.save()
            return render(request, 'user/verifyemail.html', {'verifysuccess': True})
        else:
            return render(request, 'user/verifyemail.html', {'verifyfail': True})
        return render(request, 'user/verifyemail.html')
#Logout
class LogoutView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/login')
        logout(request)
        return redirect('/login')
#Forgot password
class ForgotPasswordView( View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'user/forgotpassword.html')
class SendMailForgotPassword( APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            current_site = get_current_site(request)
            try:
                user = customer.objects.get(email=email)
            except customer.DoesNotExist:
                user=None
            mail_subject = 'Đặt lại mật khẩu của bạn'
            message = render_to_string('email/resetpassword.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = user.email
            send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [to_email])
            return Response({'status':True})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ResetPassWord(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = customer.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, customer.DoesNotExist):
            user = None
        if user is not None and default_token_generator.check_token(user, token):
            return render(request, 'user/resetpassword.html',{'id':user.id})
        return HttpResponse("404 NOT FOUND")
class ChangePassword(APIView):
    def put(self, request):
       serializer = ChangePasswordSerializer(data=request.data)
       if serializer.is_valid():
           password = serializer.validated_data['password']
           id = serializer.validated_data['id']
           user = customer.objects.get(id=id)
           user.password = password
           user.save()
           return Response({'status':True})
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ViewCustomerDashboard(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/login')
            # danh muc
        categories = category.objects.all()
        customer=request.user
        order_total=order.objects.filter(customer=customer).count()
        context={'customer':customer, 'order_total':order_total,'categories':categories}
        return render(request, 'user/dashboard.html',context)
class ViewCustomerOrder(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/login')
            # danh muc
        categories = category.objects.all()
        customer = request.user
        order_list=order.objects.filter(customer=customer)
        status_choice = order.STATUS_CHOICES
        context={'order_list':order_list,'categories':categories,'status_choice':status_choice,'customer':customer}

        return render(request, 'user/order.html',context)
class ViewChangePassword(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/login')
        customer=request.user
        # danh muc
        categories = category.objects.all()
        return render(request, 'user/changepassword.html',{'cur_password':customer.password,"id":customer.id,'categories':categories})


