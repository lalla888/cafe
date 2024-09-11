from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name=models.CharField(max_length=20)
    number=models.IntegerField()
    members=models.IntegerField()
    date=models.DateField()

class burgers(models.Model):
    head=models.CharField(max_length=25)
    price=models.IntegerField()
    offers=models.CharField(max_length=25)
    img1=models.FileField(upload_to='Media/',default=None,null=True,max_length=250)

class beverage(models.Model):
    head=models.CharField(max_length=25)
    price=models.IntegerField()
    offers=models.CharField(max_length=25)
    img1=models.FileField(upload_to='Media/',default=None,null=True,max_length=250)

class sandwich(models.Model):
    head=models.CharField(max_length=25)
    price=models.IntegerField()
    offers=models.CharField(max_length=25)
    img1=models.FileField(upload_to='Media/',default=None,null=True,max_length=250)

class frenchfries(models.Model):
    head=models.CharField(max_length=25)
    price=models.IntegerField()
    offers=models.CharField(max_length=25)
    img1=models.FileField(upload_to='Media/',default=None,null=True,max_length=250)

class dessert(models.Model):
    head=models.CharField(max_length=25)
    price=models.IntegerField()
    offers=models.CharField(max_length=25)
    img1=models.FileField(upload_to='Media/',default=None,null=True,max_length=250)

class pizzas(models.Model):
    head=models.CharField(max_length=25)
    price=models.IntegerField()
    offers=models.CharField(max_length=25)
    img1=models.FileField(upload_to='Media/',default=None,null=True,max_length=250)