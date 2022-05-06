from rest_framework import serializers
from base.models import Room, Message, Topic, User


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('host', 'topic', 'participants', 'name', 'description')