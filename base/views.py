from django.shortcuts import get_object_or_404, render
from .models import Room

# Create your views here.
def RoomView(request, id):
    # room = Room.objects.get(pk=id)
    room = get_object_or_404(Room, pk=id)
    context = {'room': room}
    return render(request, './base/room.html', context)

def Home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, './base/home.html', context)