from django.urls import path
# from .views import Home, Room
from . import views 

urlpatterns = [
    path('login/', views.loginPage, name='login' ),
    path('logout/', views.logoutUser, name='logout' ),
    path('register/', views.registerUser, name='register'),

    path('', views.Home, name='home_index'),
    path('room/<int:id>/', views.RoomView, name='room_detail'),
    path('profile/<int:id>/', views.userProfile, name='user-profile'),
    path('update-profile/', views.updateUser, name='update-profile'),

    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<int:id>', views.updateRoom, name='update-room'),
    path('delete-room/<int:id>', views.deleteRoom, name='delete-room'),
    path('delete-message/<int:id>', views.deleteMessage, name='delete-message'),
    path('topics/', views.topicsPage, name='topics'),
    path('activity/', views.activityPage, name='activity'),


]