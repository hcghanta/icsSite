from django import forms
from .models import Inventory

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = (
            'item_name', 'quantity', 'location', 'item_position', 'category', 'vendor', 'vendor_id',
            'link', 'unit_price')

class UploadFileForm(forms.Form):
    file = forms.FileField()
