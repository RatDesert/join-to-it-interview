from factory import Faker
from factory.django import DjangoModelFactory

from src.apps.users.models import User


class UserFactory(DjangoModelFactory):
    email = Faker("ascii_company_email")
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    # faker provides bad phone numbers

    class Meta:
        model = User
        django_get_or_create = ("email",)
