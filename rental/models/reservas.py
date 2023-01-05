from django.db import models
from rental.models.base_model import BaseModel
from rental.models.anuncios import Anuncios


class Reservas(BaseModel):
    anuncio = models.ForeignKey(to=Anuncios, related_name="reserva", on_delete=models.CASCADE, blank=False, null=False)
    data_check_in = models.DateField(blank=False, null=False)
    data_check_out = models.DateField(blank=False, null=False)
    valor_total = models.DecimalField(blank=False, null=False, max_digits=12, decimal_places=2)
    comentarios = models.TextField()
    qtde_hospedes = models.PositiveIntegerField(blank=False, null=False)

    class Meta:
        verbose_name_plural = "Reservas"

    def __str__(self):
        return f"Reservas {self.id} - Anuncio: {self.anuncio.nome_plataforma}, Imóvel: {self.anuncio.imovel.id}"
