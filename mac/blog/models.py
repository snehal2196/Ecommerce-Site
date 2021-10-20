from django.db import models

# Create your models here.

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    head0 = models.CharField(max_length=500)
    content0 = models.CharField(max_length=5000,default="")
    head1 = models.CharField(max_length=500)
    content1 = models.CharField(max_length=5000, default="")
    head2 = models.CharField(max_length=500)
    content2 = models.CharField(max_length=5000, default="")
    date = models.DateField()
    thumbnail = models.ImageField(upload_to='shop/images',default='')

    def __str__(self):
        return self.title
