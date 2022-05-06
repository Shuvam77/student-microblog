from django.shortcuts import render

from rest_framework import generics
from base.models import User, Topic, Room, Message
from .serializers import RoomSerializer

# Create your views here.

class RoomAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


