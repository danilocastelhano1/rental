from rest_framework import routers
from django.urls import include, path
from rental.views.ImoveisViewSet import ImoveisViewset
from rental.views.AnunciosViewSet import AnunciosViewset
from rental.views.ReservasViewSet import ReservasViewset


router = routers.DefaultRouter()
router.register(r"imoveis", ImoveisViewset)
router.register(r"anuncios", AnunciosViewset)
router.register(r"reservas", ReservasViewset)


urlpatterns = [
    path(r"rental/", include(router.urls)),
]
