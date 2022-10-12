import factory

from .models import Article
from users.factories import UserFactory

class ArticleFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('sentence')
    author = factory.SubFactory(UserFactory)
    summary = factory.Faker('paragraph')
    content = factory.Faker('text')
    slug = factory.Faker('slug')

    class Meta:
        model = Article
