from django.db import models
from datetime import datetime

class Role(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.name} - {self.role}"


class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=50,null=True)
    state = models.CharField(max_length=50)
    last_order = models.DateField(null=True, blank=True)
    total_orders = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {self.city}"
    
    class Meta:
        ordering = ['name']


class Order(models.Model):
    order_by = models.ForeignKey(Customer, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=25, default='ACTIVE')
    scheduled_date = models.DateField(null=True)
    delivered_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.order_by} at {self.timestamp.date()}"

class Product(models.Model):
    name = models.CharField(max_length=50)
    weight = models.IntegerField()
    per_box = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.weight} gm)  (Per Box = {self.per_box})"
    
    class Meta:
        ordering = ['name']
        
    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        
        if not RequiredItem.objects.filter(item=self).exists():
            RequiredItem.objects.create(item=self, required_quantity=0)
    
    
class RequiredItem(models.Model):
    item = models.ForeignKey(Product, on_delete = models.CASCADE)
    required_quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.item.name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    ordered_quantity = models.IntegerField()
    delivered_quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return f"#{self.order.id} {self.item}"
    















# class Product(models.Model):
#     product_name = models.CharField(max_length=255)
#     product_id = models.CharField(max_length=50, unique=True)
#     box_size = models.IntegerField()

#     def __str__(self):
#         return self.product_name


# class Customer(models.Model):
#     name = models.CharField(max_length=255)
#     customer_id = models.CharField(max_length=50, unique=True)
#     address = models.TextField()
#     city = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


# class Order(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     order_id = models.CharField(max_length=100, unique=True)
#     order_time = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.order_id + "By " + self.customer


# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField()

#     def __str__(self):
#         return f"{self.quantity} of {self.product.product_name} in {self.order.order_id}"


