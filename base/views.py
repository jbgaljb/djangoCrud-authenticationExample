from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers
from .models import Product
from rest_framework import status

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'desc', 'price', 'createdTime']


@api_view(['GET'])
def index(req):
    return Response('hello')

# list all products
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

# create a new product
@api_view(['POST'])
def product_create(request):
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# retrieve by id
@api_view(['GET'])
def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

# Update a product by ID
@api_view(['PUT'])
def product_update(request, pk):
    product = Product.objects.get(pk=pk)
    serializer = ProductSerializer(product, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete a product by ID
@api_view(['DELETE'])
def product_delete(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

