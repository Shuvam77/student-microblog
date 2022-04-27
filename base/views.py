from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from base.forms import RoomForm
from .models import Room, Topic, Message
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def loginPage(request):

    page = 'login'
    if request.user.is_authenticated:
        return redirect('home_index')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
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

    context = {'page':page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home_index')


def registerUser(request):
    form = UserCreationForm()
    context = {'form':form}

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home_index')
        else:
            messages.error(request, 'An error occured!')

        
    return render(request, 'base/login_register.html', context)


def RoomView(request, id):
    # room = Room.objects.get(pk=id)
    room = get_object_or_404(Room, pk=id)
    room_messages = room.message_set.all().order_by('-created')
    participants = room.participants.all()

    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            room = room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room_detail', id=room.id)

    context = {'room': room, 'room_messages': room_messages, 'participants':participants}
    return render(request, './base/room.html', context)


def Home(request):
    query = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
            Q(topic__name__icontains=query)|Q(name__icontains=query)|Q(description__icontains=query))

    # rooms = Room.objects.all()
    topics = Topic.objects.all().annotate(num_of_topic = Count('room')).order_by('-num_of_topic')

    room_messages = Message.objects.filter(
                    Q(room__topic__name__icontains=query))

    room_count = rooms.count()

    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count, 'room_messages': room_messages}
    return render(request, './base/home.html', context)

@login_required(login_url='login')
def userProfile(request, id):
    user = get_object_or_404(User, pk=id)
    rooms = user.room_set.all()
    topics = Topic.objects.all().annotate(num_of_topic = Count('room')).order_by('-num_of_topic')
    room_message = user.message_set.all()

    room_count = rooms.count()

    context = {'user': user, 'rooms': rooms, 'topics':topics, 'room_messages': room_message, 'room_count': room_count}
    return render(request, 'base/profile.html', context)


@login_required(login_url='login')
def createRoom(request):
    form = RoomForm
    topics = Topic.objects.all()
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description')
        )
        return redirect('home_index')

        # form = RoomForm(request.POST)
        # if form.is_valid():
        #     context = form.save(commit=False)
        #     context.host = request.user
        #     context.save()
        #     return redirect('home_index')

    context={'form': form, 'topics':topics}
    return render(request, 'base/room_form.html', context)


@login_required(login_url='login')
def updateRoom(request, id):
    room = get_object_or_404(Room, pk=id)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()

    if request.user != room.host:
        return HttpResponse('You are not allowed to make changes!!')

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)

        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()

        return redirect('home_index')

    # if request.method == 'POST':
    #     form = RoomForm(request.POST, instance=room)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('home_index')
    
    context={'form': form, 'topics':topics, 'room':room}
    return render(request, 'base/room_form.html', context)


@login_required(login_url='login')
def deleteRoom(request, id):
    room = get_object_or_404(Room, pk=id)

    if request.user != room.host:
        return HttpResponse('You are not allowed to make changes!!')

    if request.method == 'POST':
        room.delete()
        return redirect('home_index')

    context = {'obj':room}
    return render(request, 'base/delete.html',context)


@login_required(login_url='login')
def deleteMessage(request, id):
    message = get_object_or_404(Message, pk=id)

    if request.user != message.user:
        return HttpResponse('You are not allowed to make changes!!')

    if request.method == 'POST':
        message.delete()
        return redirect('room_detail', id=message.room.id)

    context = {'obj':message}
    return render(request, 'base/delete.html',context)