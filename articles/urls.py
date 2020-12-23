from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='index'),
    path('article_create', views.AricleCreate.as_view(), name='article_create'),
    path('artcle_detail/<slug:slug>', views.ArticleDetail.as_view(),name='article_detail'),

]