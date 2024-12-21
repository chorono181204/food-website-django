from django.db import models
# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    details = models.TextField()
    image = models.ImageField(upload_to="images",default=None,null=True,blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
class product(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    details = models.TextField()
    price = models.IntegerField(default=0)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images")
    calories=models.IntegerField(default=0)
    protein=models.IntegerField(default=0)
    fats=models.IntegerField(default=0)
    carbs=models.IntegerField(default=0)
    isNew=models.BooleanField(default=False,null=True,blank=True)
    isSale=models.BooleanField(default=False,null=True,blank=True)
    discount=models.IntegerField(default=0,null=True,blank=True)
    def __str__(self):
        return self.name
    @property
    def afterDiscount(self):
        return int( (1-self.discount/100)*self.price)

