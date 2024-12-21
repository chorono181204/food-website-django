from django.urls import path
from .views import ViewLogin, CheckEmail, SignUp, VerifyEmail, ActiveAccount, LogoutView, ForgotPasswordView, \
    ResetPassWord, SendMailForgotPassword, ChangePassword, ViewCustomerDashboard, ViewCustomerOrder, ViewChangePassword

app_name='user'
urlpatterns=[
path('login/',ViewLogin.as_view(),name='login'),
path('api/checkemail/',CheckEmail.as_view(),name='checkemail'),
path('api/signup/',SignUp.as_view(),name='signup'),
path('verifyemail/',VerifyEmail.as_view(),name='verify'),
path('activeaccount/<uidb64>/<token>/', ActiveAccount.as_view(), name='active'),
path('logout/',LogoutView.as_view(),name='logout'),
path('forgotpassword/',ForgotPasswordView.as_view(),name='forgotpassword'),
path('resetpassword/<uidb64>/<token>/',ResetPassWord.as_view(),name='resetpassword'),
path('api/sendmailforgotpassword/',SendMailForgotPassword.as_view(),name='sendmailforgotpassword'),
path('api/changepassword/',ChangePassword.as_view(),name='changepassword'),
path('customer/dashboard/',ViewCustomerDashboard.as_view(),name='customerdashboard'),
path('customer/order/',ViewCustomerOrder.as_view(),name='customerorder'),
path('customer/changepassword',ViewChangePassword.as_view(),name='customerchangepassword'),
]
