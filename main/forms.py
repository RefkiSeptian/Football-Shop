from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields =  ["name", "price", "category", "thumbnail", "description", "brand", "stok"]
        exclude = ["id"] 