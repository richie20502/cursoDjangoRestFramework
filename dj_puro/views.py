from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .models import Category
# Create your views here.

def categoria_list(request):
    MAX_OBJECTS = 20
    categorys = Category.objects.all()[:MAX_OBJECTS]
    data = {
        'res' : list(categorys.values('description','active'))
    }
    return JsonResponse(data);

def categoria_details(request, id):
    category = get_object_or_404(Category, pk=id)
    data = {
        "result": {
            'description' :category.description,
            'active': category.active
        }
    }
    category = Category.objects.get(id = id)
    return JsonResponse(data) 
