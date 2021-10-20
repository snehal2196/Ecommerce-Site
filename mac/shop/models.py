from django.db import models


# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default='')
    subcategory = models.CharField(max_length=50, default='')
    price = models.IntegerField(default=0)
    product_desc = models.TextField()
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default='')

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    name= models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    phone= models.CharField(max_length=12)
    desc= models.TextField()

    def __str__(self):
        return self.name

class Order(models.Model):
    itemJson = models.CharField(max_length=5000,default='')
    name= models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    address1= models.CharField(max_length=50)
    address2 = models.CharField(max_length=100)
    city= models.CharField(max_length=50)
    state= models.CharField(max_length=50)
    phone= models.CharField(max_length=12)
    zip_code= models.CharField(max_length=12)

    def __str__(self):
        return self.name

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    datetime = models.DateTimeField(auto_now_add=True)