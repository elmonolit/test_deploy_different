from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, View, DetailView
from . import models
from . import forms
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


class MainView(ListView):
    model = models.Article


class AricleCreate(LoginRequiredMixin, View):
    def post(self, request):
        author = models.Article(author=request.user)
        form = forms.ArticleForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))

    def get(self, request):
        form = forms.ArticleForm()
        return render(request, 'articles/article_create.html', {'form': form})


class ArticleDetail(DetailView):
    model = models.Article


# class ProfileView(ListView):
#     model = models.Article.objects.filter(author_id=1)
#     template_name = 'articles/profile.html'
#     # def get(self, request, *args, **kwargs):
#     #     print(request)

class ProfileView(LoginRequiredMixin,View):
    def get(self,request, username):
        queryset = models.Article.objects.filter(author_id=request.user)
        username = request.user
        return render(request, 'articles/profile.html', {'article_list':queryset})