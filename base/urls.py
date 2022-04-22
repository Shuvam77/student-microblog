from django.urls import path
# from .views import base
from . import views 

urlpatterns = [
    path('', views.base, name='base_index'),
]