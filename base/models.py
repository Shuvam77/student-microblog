from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    bio = models.TextField(null=True)
    email = models.EmailField(unique=True, null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

class Topic(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "topic"
        verbose_name_plural = "topics"

    def __str__(self):
        return f'{self.name}'


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ManyToManyField(Topic, blank=True, related_name='topics')
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "room"
        verbose_name_plural = "rooms"
        ordering = ['-updated', '-created']

    def __str__(self):
        return f'{self.name}'


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "message"
        verbose_name_plural = "messages"
        ordering = ['-updated', '-created']

    def __str__(self):
        return f'{self.body[0:50]} commented by {self.user.username}'
    