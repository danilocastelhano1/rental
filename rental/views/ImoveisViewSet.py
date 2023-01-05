from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from rental.models import Imoveis
from rental.serializers.ImoveisSerializer import ImoveisSerializer


class ImoveisViewset(viewsets.ModelViewSet):
    queryset = Imoveis.objects.all()
    serializer_class = ImoveisSerializer
    permission_classes = [AllowAny]
