# Generated by Django 3.1.4 on 2020-12-23 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_userprofile_usrnm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='usrnm',
        ),
    ]
