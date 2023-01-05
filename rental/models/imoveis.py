from django.db import models
from rental.models.base_model import BaseModel


class Imoveis(BaseModel):
    hospedes_limite = models.PositiveIntegerField(blank=False, null=False)
    qtde_banheiros = models.PositiveIntegerField(blank=False, null=False)
    pet_friendly = models.BooleanField(default=False, blank=False, null=False)
    valor_limpeza = models.DecimalField(blank=False, null=False, max_digits=12, decimal_places=2)
    data_ativacao = models.DateField(blank=False, null=False)

    class Meta:
        verbose_name_plural = "Imóveis"

    def __str__(self):
        return f"Imovel {self.id} - Qtde Hóspedes: {self.hospedes_limite}"
