from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from rental.models import Anuncios
from rental.serializers.AnunciosSerializer import AnunciosSerializer


class AnunciosViewset(viewsets.GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin):
    queryset = Anuncios.objects.all()
    serializer_class = AnunciosSerializer
    permission_classes = [AllowAny]
