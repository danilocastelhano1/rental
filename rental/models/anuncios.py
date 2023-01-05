from django.db import models
from rental.models.base_model import BaseModel
from rental.models.imoveis import Imoveis


class Anuncios(BaseModel):
    imovel = models.ForeignKey(to=Imoveis, related_name="anuncio", on_delete=models.CASCADE, blank=False, null=False)
    nome_plataforma = models.CharField(max_length=150, blank=False, null=False)
    taxa_plataforma = models.DecimalField(blank=False, null=False, max_digits=12, decimal_places=2)

    class Meta:
        verbose_name_plural = "Anúncios"

    def __str__(self):
        return f"Anuncios, plataforma {self.nome_plataforma}"
