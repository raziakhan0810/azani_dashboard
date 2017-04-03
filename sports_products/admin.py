from django.contrib import admin
from models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'address')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('status', 'order_id', 'product_name', 'cost_price')
