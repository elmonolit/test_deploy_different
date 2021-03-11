from articles.models import Article

from rest_framework.serializers import ModelSerializer


class ArticlesSerializer(ModelSerializer):
    class Meta:
        model = Article
        exclude = ('slug',)
