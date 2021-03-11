from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        print('aaaaa')
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    # instance.userprofile.usrnm =
    print('asdlfk')
    instance.userprofile.save()

@receiver(post_delete, sender=User)
def del_prof(sender,instance,**kwargs):
    print('deleted')

