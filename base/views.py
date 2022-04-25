from django.shortcuts import get_object_or_404, redirect, render

from base.forms import RoomForm
from .models import Room, Topic
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User doesnot exists!')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_index')
        else:
            messages.error(request, 'Username or Password doesnot match!')

    context = {}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home_index')



def RoomView(request, id):
    # room = Room.objects.get(pk=id)
    room = get_object_or_404(Room, pk=id)
    context = {'room': room}
    return render(request, './base/room.html', context)


def Home(request):
    query = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
            Q(topic__name__icontains=query)|Q(name__icontains=query)|Q(description__icontains=query))

    # rooms = Room.objects.all()
    topics = Topic.objects.all()

    room_count = rooms.count()

    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count}
    return render(request, './base/home.html', context)


def createRoom(request):
    form = RoomForm
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_index')

    context={'form': form}
    return render(request, 'base/room_form.html', context)


def updateRoom(request, id):
    room = get_object_or_404(Room, pk=id)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home_index')
    
    context={'form': form}
    return render(request, 'base/room_form.html', context)


def deleteRoom(request, id):
    room = get_object_or_404(Room, pk=id)
    context = {'room':room}
    if request.method == 'POST':
        room.delete()
        return redirect('home_index')

    return render(request, 'base/delete.html',context)