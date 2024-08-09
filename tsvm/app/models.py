from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User , on_delete=models.SET_NULL,null=True , blank=False)
    name = models.CharField(max_length=200,null=True, blank=True)
    email = models.EmailField(max_length=200,null=True, blank=True)
    def __str__(self) :
        return self.name if self.name else "unknow"
class Product(models.Model):
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField(max_length=200,null=True)
    digital = models.BooleanField(default=False ,null=True,blank=True )
    def __str__(self) :
        return self.name
class Order(models.Model):
    customer = models.ForeignKey(Customer , on_delete=models.SET_NULL,null = True , blank= False)
    date_order = models.DateTimeField(auto_now=True)
    complete = models.BooleanField(default=False ,null=True,blank=False)
    transaction_id = models.CharField(max_length=200,null = False)
    def __str__(self) :
        return str(self.transaction_id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null = True , blank= True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL , null = True , blank = True)
    quantity = models.IntegerField(default=0 , null = True , blank= True)
    date_added = models.DateTimeField(auto_now=True)
    
class Shipping_address(models.Model):
    cutomer = models.ForeignKey(Customer,on_delete=models.SET_NULL , null = True ,blank=False)
    order = models.ForeignKey(Order , on_delete= models.SET_NULL , null = True , blank= False)
    address = models.CharField(max_length=200,null=False )
    city = models.CharField(max_length=200,null=False ) 
    road = models.CharField(max_length=200,null=False ) 
    house_number = models.IntegerField(null=False , blank=True )
    state = models.CharField(max_length=200 , null = True , blank=True)
    mobile = models.CharField(max_length=10 , null=False , blank=False )
    date_of_receipt = models.DateField(auto_now_add=True  )
    def __str__(self) :
        return str(self.address)
     