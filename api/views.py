from django.http import JsonResponse
from api.serializers import ProductSerializer
from api.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all() # returns queryset
    serializer = ProductSerializer(products, many=True)  # As it's more than a single object
    # return JsonResponse({
    #     'data': serializer.data
    # })
    # DRF Browsable API
    # http://localhost:8000/api/v1/products/?format=json
    return Response(serializer.data)

@api_view(['GET'])
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    # it returns product model
    serializer = ProductSerializer(product) 
    return Response(serializer.data)