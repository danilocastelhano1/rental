from rest_framework import serializers

from rental.models import Reservas


class ReservasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservas
        fields = "__all__"
        read_only_fields = ('id', 'created', 'updated')

    def validate(self, attrs):
        check_in = attrs["data_check_in"]
        check_out = attrs["data_check_out"]

        if check_in > check_out:
            raise serializers.ValidationError("A data de Checkin tem que ser Menor ou igual que a data de Checkout")

        return attrs
