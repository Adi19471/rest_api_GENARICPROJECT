from django.db import models
from rest_framework import serializers 
from .models import ProductDetailes

class ProductDetailesSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductDetailes
        exclude = ['book_name']