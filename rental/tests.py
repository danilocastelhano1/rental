import time

from rest_framework.test import APITestCase
from django.core import management


class RentalTests(APITestCase):
    def setUp(self) -> None:
        management.call_command("seed_db")

    def test_list_imoveis(self):
        resp = self.client.get("/rental/imoveis/")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 5)

    def test_list_anuncios(self):
        resp = self.client.get("/rental/anuncios/")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 3)

    def test_list_reserva(self):
        resp = self.client.get("/rental/reservas/")
        self.assertEqual(resp.status_code, 200)
        print('danilo', len(resp.json()))
        self.assertEqual(len(resp.json()), 8)

    def test_shoud_error_when_creating_reservas_with_checkin_greather_than_checkout(self):
        data = {
            "data_check_in": "2022-01-06",
            "data_check_out": "2022-01-05",
            "valor_total": 59.99,
            "comentarios": "TestCase",
            "qtde_hospedes": 5,
            "anuncio": 1

        }
        resp = self.client.post("/rental/reservas/", data=data)
        self.assertEqual(resp.status_code, 400)

    def test_shoud_success_when_creating_reservas_with_checkin_less_than_checkout(self):
        data = {
            "data_check_in": "2022-01-04",
            "data_check_out": "2022-01-05",
            "valor_total": 59.99,
            "comentarios": "TestCase",
            "qtde_hospedes": 5,
            "anuncio": 1

        }
        resp = self.client.post("/rental/reservas/", data=data)
        self.assertEqual(resp.status_code, 201)
