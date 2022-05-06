from django.urls import path

from api.views import RoomAPIView


urlpatterns = [
    path('', RoomAPIView.as_view(), name="room:apiroom_list")
]