from django.db import models
from django.template.defaultfilters import slugify
from transliterate import translit
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    img = models.ImageField(upload_to='articles', blank=True)
    slug = models.SlugField(blank=True,unique=True)

    def get_absolute_url(self):
        return reverse('article_detail',kwargs={'slug':self.slug})

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(translit(self.title,'ru',reversed=True))
        super(Article,self).save()

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

