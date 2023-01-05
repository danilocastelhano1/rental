from rest_framework import serializers

from rental.models import Imoveis


class ImoveisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imoveis
        fields = "__all__"
        read_only_fields = ('id', 'created', 'updated')
