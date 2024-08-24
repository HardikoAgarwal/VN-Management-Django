from django.contrib import admin

# Register your models here.
from .models import  Customer, Order, Product, OrderItem, User, Role

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(User)
admin.site.register(Role)