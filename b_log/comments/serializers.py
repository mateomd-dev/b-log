from rest_framework import serializers

from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'article', 'parent', 'created_at', 'visible']
                
