from django.db import models
from django.template.defaultfilters import slugify
from transliterate import translit
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_delete, post_save


class Article(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    img = models.ImageField(upload_to='articles', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(blank=True, unique=True)

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None,):
        # self.author =
        self.slug = slugify(translit(self.title, 'ru', reversed=True))
        super(Article, self).save()

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'






# def art_del(sender, instance, **kwargs):
#     print('deleted')
#
#
# post_delete.connect(art_del, sender=Article)
#
#
# def art_create(sender, instance, **kwargs):
#     print('created')


# post_save.connect(art_create, sender=Article)
