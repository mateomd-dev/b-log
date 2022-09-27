from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255, unique=True)
    summary = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()
    meta_desc = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
