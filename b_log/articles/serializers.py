from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'content', 'owner', 'summary', 'created_at', 'comments']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    articles = serializers.HyperlinkedRelatedField(many=True, view_name='article-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'articles']
