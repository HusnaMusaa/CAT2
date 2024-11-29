from django.db import models
from django.contrib.auth.models import Customer


# Create your models here.
# Represents an order placed by a customer.
class Order(models.Model):
    # ForeignKey relationship to the Customer model.
    # This indicates that each order is associated with one customer.

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # Date when the order was placed, automatically set to the current date when the order is created.
    order_date = models.DateField(auto_now_add=True)
    # Total amount of the order, stored as a decimal number with up to 10 digits and 2 decimal places.
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    # Returns a string representation of the order, including the order ID and associated customer's name.
    def _str_(self):
        return f"Order #{self.id} - {self.customer}"