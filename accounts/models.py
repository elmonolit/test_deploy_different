from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # usrnm = models.CharField(max_length=200)
    email = models.EmailField(blank=True, default='email@company.com')
    pic = models.ImageField(upload_to='userpics',blank=True, default='default.png')


    
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'