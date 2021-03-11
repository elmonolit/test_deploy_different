from django.shortcuts import render

from .serializers import ArticlesSerializer
from articles.models import Article

from rest_framework.viewsets import ModelViewSet


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer
# Create your views here.
