from django.urls import path

from api.views import RoomAPIView, RoomDetailAPIView, RoomDeleteAPIView, RoomCreateAPIView


urlpatterns = [
    path('', RoomAPIView.as_view(), name="room:apiroom_list"),
    path('<int:pk>', RoomDetailAPIView.as_view(), name="room:apiroom_detail"),
    path('del/<int:pk>', RoomDeleteAPIView.as_view(), name="room:apiroom_delete"),
    path('create', RoomCreateAPIView.as_view(), name="room:apiroom_create" )
]