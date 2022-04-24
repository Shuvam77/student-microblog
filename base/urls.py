from django.urls import path
# from .views import Home, Room
from . import views 

urlpatterns = [
    path('', views.Home, name='home_index'),
    path('room/<int:id>/', views.RoomView, name='room_detail'),

]