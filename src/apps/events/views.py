from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from src.apps.events.exceptions import UserAlreadyRegisteredForEvent
from src.apps.events.filters import EventsFilterSet
from src.apps.events.models import Event
from src.apps.events.permissions import IsOwnerOrReadOnly
from src.apps.events.serializers import CreateEventSerializer, ListEventSerializer


@extend_schema_view(
    register=extend_schema(responses=None, request=None),
    destroy=extend_schema(responses=None),
)
class EventViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Event.objects.select_related("organizer").prefetch_related("participants")
    filterset_class = EventsFilterSet
    search_fields = [
        "title",
        "description",
        "location",
        "organizer__email",
        "organizer__last_name",
        "organizer__first_name",
    ]

    def get_serializer_class(self):
        match self.action:
            case "list" | "retrieve":
                return ListEventSerializer
            case "create" | "update" | "partial_update":
                return CreateEventSerializer

    def get_serializer_context(self):
        return {"user": self.request.user}

    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def register(self, request, pk=None):
        user = request.user
        event = self.get_object()
        try:
            event.add_participant(user)
        except UserAlreadyRegisteredForEvent as e:
            return Response(data=e.message, status=status.HTTP_409_CONFLICT)
        return Response(status=status.HTTP_204_NO_CONTENT)
