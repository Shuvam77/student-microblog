from django.urls import path
# from .views import Home, Room
from . import views 

urlpatterns = [
    path('', views.Home, name='home_index'),
    path('room/<int:id>/', views.RoomView, name='room_detail'),
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<int:id>', views.updateRoom, name='update-room'),
    path('delete-room/<int:id>', views.deleteRoom, name='delete-room'),

]