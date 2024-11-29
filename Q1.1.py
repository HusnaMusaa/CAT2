from django.db import models

# Create your models here.

class Customer(models.Model):  # One customer can make many orders
    # stored as a string with a maximum length of 100 characters.
    name = models.CharField(max_length=100)
    #  must be unique in the database to avoid duplicates
    email = models.EmailField(unique=True)

    # Returns a string representation of the customer
    def _str_(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return f"Order #{self.id} - {self.customer}"