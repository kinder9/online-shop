from .models import Category,Product
from rest_framework import serializers


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','category_image','category_name']


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','product_name','price','owner','phone_number','product_image','product_type',
                  'description','created_date']