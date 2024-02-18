from rest_framework import viewsets, mixins
from src.apps.users.serializers import CreateUserSerializer
from src.apps.users.models import User


class UserRegistrationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()
    authentication_classes = []
    permission_classes = []
