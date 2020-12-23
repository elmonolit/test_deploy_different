from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView,View,DetailView
from . import models
from . import forms
from django.urls import reverse

class MainView(ListView):
    model = models.Article

class AricleCreate(View):
    def post(self,request):
        form = forms.ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))

    def get(self,request):
        form = forms.ArticleForm()
        return render(request, 'articles/article_create.html', {'form':form})

class ArticleDetail(DetailView):
    model = models.Article
