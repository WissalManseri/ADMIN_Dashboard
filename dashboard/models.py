from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.name} by {self.user.username}'

class Signup(models.Model):
    date = models.DateField()
    signups = models.IntegerField()

class SignupAdmin(admin.ModelAdmin):
    list_display = ('date', 'signups')

admin.site.register(Signup, SignupAdmin)

admin.site.register(User)

admin.site.register(Order)
