from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, View, DetailView
from . import models
from . import forms
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


class MainView(ListView):
    model = models.Article
    def get(self,request,*args,**kwargs):
        print(self.request.GET)
        a = self.request.GET
        print(a)
        return super(MainView,self).get(request,*args,**kwargs)

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

def get_list(max_res,starts_with=''):
    article_list = []
    if starts_with:
        article_list = models.Article.objects.filter(title__istartswith=starts_with)
    if max_res > 0:
        if len(article_list) > max_res:
            article_list = article_list[:max_res]
    return article_list


def search(request):
    article_list = []
    if  request.method == 'GET':
        starts_with = request.GET['search_bar']
        article_list = get_list(8,starts_with)
    return render(request,'articles/e.html', {'search_list':article_list})

# def srch(request):
