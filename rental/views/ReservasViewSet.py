from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from rental.models import Reservas
from rental.serializers.ReservasSerializer import ReservasSerializer


class ReservasViewset(viewsets.GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      mixins.DestroyModelMixin):
    queryset = Reservas.objects.all()
    serializer_class = ReservasSerializer
    permission_classes = [AllowAny]
