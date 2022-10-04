from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Article

class DynamicArticleSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super().__init__(*args, **kwargs)
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for f in existing - allowed:
                self.fields.pop(f)

class ArticleSerializer(DynamicArticleSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Article
        fields = ['title', 'author',  'summary', 'created_at']
