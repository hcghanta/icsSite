from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Inventory(models.Model):
    item_name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    item_position = models.CharField(max_length=50, null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    vendor = models.CharField(max_length=50, null=True, blank=True)
    vendor_id = models.CharField(max_length=20, null=True, blank=True)
    link = models.CharField(max_length=100, null=True, blank=True )
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    updated_date = models.DateField(default=datetime.date.today())

    def updated(self):
        self.updated_date = datetime.date.today()
        self.save()

    def __str__(self):
        return str(self.item_name)

    def total_values(self):
        return self.unit_price * self.quantity
