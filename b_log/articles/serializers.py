from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'author', 'summary', 'created_at']

