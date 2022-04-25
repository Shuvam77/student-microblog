from django.contrib import admin

from base.models import Room, Topic, Message

# Register your models here.

class CustomPermissionMixin:
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields['name'].disabled = True
        return form

    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request):
        return False


class RoomAdmin(CustomPermissionMixin, admin.ModelAdmin):
    list_disply = ('name', 'description')
    readonly_field = ('created', 'updated')

admin.site.register(Room, RoomAdmin)

admin.site.register(Topic)
admin.site.register(Message)
