from . import models
from django import forms

class ArticleForm(forms.ModelForm):

    class Meta:
        model = models.Article
        exclude = ('slug','author')
