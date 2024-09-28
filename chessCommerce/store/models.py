from django.db import models
import datetime 

'''
## Models
- Category
- Customer 
- Product
- Order 
'''


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 


class Customer(models.Model):
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    phone_number = models.CharField(max_length=10, default='')
    email = models.EmailField(max_length=100, default='default@example.com')
    password = models.CharField(max_length=100, default='')

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.phone_number}'


class Product(models.Model):
    name = models.CharField(max_length=100, default='')
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/', default='')

    def __str__(self):
        return self.name 


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default='')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default='')
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    date = models.DateField(default=datetime.date.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'Order of {self.quantity} {self.product.name}(s) for {self.customer.first_name}'
