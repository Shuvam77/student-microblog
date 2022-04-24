from django.contrib import admin

from base.models import Room, Topic, Message

# Register your models here.


class RoomAdmin(admin.ModelAdmin):
    list_disply = ('name', 'description', 'created', 'updated')
    readonly_field = ('created', 'updated')
admin.site.register(Room, RoomAdmin)

admin.site.register(Topic)
admin.site.register(Message)
