from django.contrib import admin

from rental.models import Anuncios, Imoveis, Reservas
# Register your models here.

admin.site.register(Anuncios)
admin.site.register(Imoveis)
admin.site.register(Reservas)
