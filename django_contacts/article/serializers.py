from rest_framework import serializers
from .models import Article, Author


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id_db_article', 'title', 'description', 'body', 'author_id')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'email', 'id_db_author')
