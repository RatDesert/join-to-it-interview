from rest_framework import mixins, viewsets

from src.apps.users.models import User
from src.apps.users.serializers import CreateUserSerializer


class UserRegistrationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()
    authentication_classes = []
    permission_classes = []
