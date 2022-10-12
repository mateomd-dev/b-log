from django.test import TestCase

from .models import Article
from .factories import ArticleFactory

class ArticleTestCase(TestCase):
    def test_str(self):
        article = ArticleFactory()
        self.assertEquals(str(article), article.title)
