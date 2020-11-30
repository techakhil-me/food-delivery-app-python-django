from django.db import models

# Create your models here.
class tomato_user(models.Model):
    username = models.CharField(max_length=200)
    def __str__(self):
        return f'Username = {self.username}, Cart = {list(self.cart_set.all())}'

class cart(models.Model):
    user = models.ForeignKey(tomato_user, on_delete=models.CASCADE)
    product = models.CharField(max_length=200)
    quantity =  models.CharField(max_length=20)
    price = models.CharField(max_length=255)

    def __str__(self):
      return f'Product = {self.product}, Quantity= {self.quantity}'

