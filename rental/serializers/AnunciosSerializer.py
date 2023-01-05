from rest_framework import serializers

from rental.models import Anuncios


class AnunciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncios
        fields = "__all__"
        read_only_fields = ('id', 'created', 'updated')
