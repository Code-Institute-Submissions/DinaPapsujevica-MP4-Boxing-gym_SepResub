from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=500)
    sku = models.CharField(max_length=40, null=True, blank=True)
    image_link = models.ImageField(null=True, blank=True, upload_to='static/uploaded_images')
    name = models.CharField(max_length=500, null=True)
    sizes = models.CharField(max_length=500, null=True)
    price = models.FloatField(null=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return str(self.name)
