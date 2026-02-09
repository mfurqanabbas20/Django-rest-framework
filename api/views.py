from django.http import JsonResponse
from api.serializers import ProductSerializer
from api.models import Product

def product_list(request):
    products = Product.objects.all() # returns queryset
    serializer = ProductSerializer(products, many=True)  # As it's more than a single object
    return JsonResponse({
        'data': serializer.data
    })