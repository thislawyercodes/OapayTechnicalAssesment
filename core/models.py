from decimal import Decimal
from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=255,null=False,blank=False)
    email=models.EmailField(unique=True,null=False,blank=False)

class Orders(models.Model):
    customer=models.ForeignKey(to=Customer,blank=False,null=False,on_delete=models.CASCADE) #todo:what happens on delete do we delete associated orders for now cascade
    product_name=models.CharField(max_length=255,null=False,blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    created_at = models.DateTimeField(auto_now_add=True)








