from django.contrib import admin
from .models import Signup, User, Order

# Register your models here.

@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_date')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'created_date')
    search_fields = ('username', 'email')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'created_date')
    list_filter = ('created_date',)
    search_fields = ('user__username', 'product')