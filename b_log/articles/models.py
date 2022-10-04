from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255, unique=True)
#    author = models.ForeignKey('auth.User', related_name='articles', on_delete=models.CASCADE)
    summary = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, unique=True)
    meta_desc = models.CharField(max_length=150, blank=True)
