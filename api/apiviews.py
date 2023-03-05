from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Producto
from .serializers import ProductoSerializer

class ProductoList(APIView):
    def get(self, request):
        prod = Producto.objects.all()
        data = ProductoSerializer(prod, many= True).data
        return Response(data)

class ProductoDetalle(APIView):
    def get(self, request,pk):
        prod = get_object_or_404(Producto,pk=pk)
        data = ProductoSerializer(prod).data
        return Response(data)