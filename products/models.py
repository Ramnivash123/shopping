from django.db import models

# Create your models here.
class Products(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    category=models.CharField(max_length=100)
    image=models.CharField(max_length=100)

class Cart(models.Model):
    u_id=models.IntegerField()
    p_id=models.IntegerField()
    qty=models.IntegerField()
    status=models.IntegerField()
    address=models.CharField(max_length=100, null=True, blank=True)
    ord_date=models.DateField(null=True)
