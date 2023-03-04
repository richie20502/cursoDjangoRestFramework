from django.urls import path
from dj_puro import views

urlpatterns = [
    path('category/',views.categoria_list,name='list_category'),
    path('category/<int:id>',views.categoria_list,name='detail_category'),
]
