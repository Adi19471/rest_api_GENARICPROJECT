from django.shortcuts import render

# Create your views here.



from .models import ProductDetailes 

from .serializers import ProductDetailesSerializers

from rest_framework import generics





class ProductListView(generics.ListCreateAPIView):
    queryset = ProductDetailes.objects.all()
    serializer_class = ProductDetailesSerializers


class ProductDetailesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductDetailes.objects.all()
    serializer_class = ProductDetailesSerializers


