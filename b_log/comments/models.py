from django.db import models

from articles.models import Article

class Comment(models.Model):
    #    author = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name='replies', on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return '[%d] %s: %s' % (self.id, self.content)
