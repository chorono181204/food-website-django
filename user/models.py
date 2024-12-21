from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class customer(AbstractUser):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)
    is_authenticated=models.BooleanField(default=False)
    first_name = models.CharField(max_length=50, null=True,blank=True)
    last_name = models.CharField(max_length=50, null=True,blank=True)
    username=models.CharField(max_length=50,null=True,blank=True,unique=True)
    customer_code=models.CharField(max_length=50,null=True,blank=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
    def __str__(self):
        return self.email