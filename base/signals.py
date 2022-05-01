# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Room, Topic

# @receiver(post_save, sender=Room)
# def pre_save_topic_room(sender, instance, created, **kwargs):

#     if created:
#         topic = Topic.objects.bulk_create(room=instance)
