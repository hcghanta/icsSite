from django.contrib import admin
from .models import Inventory

class InventoryList(admin.ModelAdmin):
    list_display = ('item_name', 'quantity', 'item_position', 'category')
    list_filter = ('item_position', 'category')
    search_fields = ('item_name', 'category', 'item_position')
    ordering = ['category']

# Register your models here.
admin.site.register(Inventory, InventoryList)
