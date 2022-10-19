from .models import User

import factory

class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker("first_name")
    password = factory.Faker("password")
    email = factory.Faker("email")

    class Meta:
        model = User
