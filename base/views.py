from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers
from .models import Product, Student
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'desc', 'price', 'createdTime']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'email', 'age', 'createdTime']


@api_view(['GET'])
def index(req):
    return Response('hello')

# list all products
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

#-----------------------------------------------------------------

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

#-----------------------------------------------------------------------

# list all students
@api_view(['GET'])
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

# create a new product
@api_view(['POST'])
def student_create(request):
    serializer = StudentSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# retrieve by id
@api_view(['GET'])
def student_detail(request, pk):
    product = Student.objects.get(pk=pk)
    serializer = StudentSerializer(product)
    return Response(serializer.data)

# Update a product by ID
@api_view(['PUT'])
def student_update(request, pk):
    student = Student.objects.get(pk=pk)
    serializer = StudentSerializer(student, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete a product by ID
@api_view(['DELETE'])
def student_delete(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
