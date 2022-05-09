from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from base.models import User, Topic, Room, Message
from .serializers import RoomSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class RoomAPIView(generics.ListAPIView):
    queryset = Room.objects.all().order_by('-created')
    serializer_class = RoomSerializer


class RoomDetailAPIView(generics.RetrieveAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        return Room.objects.all()


class RoomDeleteAPIView(generics.DestroyAPIView):
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Room.objects.filter(host = self.request.user.id)
        return queryset


class RoomCreateAPIView(generics.CreateAPIView):
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]
    # queryset = Room.objects.all()

    def perform_create(self, serializer):
        host = get_object_or_404(User, id=self.request.user.id)
        return serializer.save(host = host)

# Haven't completed this one need to do more research and after that complete the api setting.




