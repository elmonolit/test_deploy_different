from .models import Article
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver


def art_del(sender, instance, **kwargs):
    print('deleted')


post_delete.connect(art_del, sender=Article)


def art_create(sender, instance, **kwargs):
    print('created')


post_save.connect(art_create, sender=Article)
