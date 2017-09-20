from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField('Quantity available', default=0)
    description = models.TextField(default='Description of this product')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:product_detail', kwargs={'pk': self.id})

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField(default=0)
    complete = models.BooleanField(default=False)

    def __str__(self):
        try:
            return ('{}s in {}\'s cart'.format(self.product.name, self.user.name))
        except:
            return ('{}s in My cart'.format(self.product.name))
    def get_absolute_url(self):
        return reverse('products:cart_detail', kwargs={'pk': self.id})