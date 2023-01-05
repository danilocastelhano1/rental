import random
from django.contrib.auth.models import User
from datetime import date, timedelta
from django.core.management.base import BaseCommand
from rental.models import Imoveis
from rental.models import Anuncios
from rental.models import Reservas


class Command(BaseCommand):
    help = 'Seed the database as the assessment requires'

    def insert_imoveis(self):
        if Imoveis.objects.count() > 0:
            return

        self.stdout.write(self.style.WARNING('Iniciando o processo de Inserção de Imóveis'))

        Imoveis.objects.all().delete()
        for i in range(5):
            Imoveis.objects.create(
                hospedes_limite=random.randint(1, 10),
                qtde_banheiros=random.randint(1, 5),
                pet_friendly=True if i in [0, 2] else False,
                valor_limpeza=random.uniform(100.00, 1000.50),
                data_ativacao=date.today()
            )
        self.stdout.write(self.style.SUCCESS('processo de Inserção de Imóveis Finalizado'))

    def insert_anuncios(self):
        if Anuncios.objects.count() > 0:
            return

        self.stdout.write(self.style.WARNING('Iniciando o processo de Inserção de Anuncios'))

        Anuncios.objects.all().delete()
        for i in range(3):
            Anuncios.objects.create(
                nome_plataforma=f"Plataforma {i + 1}",
                taxa_plataforma=random.uniform(1.30, 49.99),
                imovel=Imoveis.objects.all()[i]
            )
        self.stdout.write(self.style.SUCCESS('processo de Inserção de Anuncios Finalizado'))

    def insert_reservas(self):
        if Reservas.objects.count() > 0:
            return

        self.stdout.write(self.style.WARNING('Iniciando o processo de Inserção de Reservas'))

        Reservas.objects.all().delete()
        for i in range(8):
            Reservas.objects.create(
                data_check_in=date.today(),
                data_check_out=date.today() + timedelta(days=i + 1),
                valor_total=random.uniform(49.99, 120.99),
                comentarios=f"Um comentário aleatório qualquer {i + 1}",
                qtde_hospedes=random.randint(1, 12),
                anuncio=Anuncios.objects.all()[random.randint(0, 2)]
            )

        self.stdout.write(self.style.SUCCESS('processo de Inserção de Anuncios Finalizado'))

    def create_super_user(self):
        if User.objects.count() == 0:
            self.stdout.write(self.style.WARNING('Iniciando o processo de Inserção de Super User'))
            User.objects.create_superuser('admin', 'admin@example.com', 'mystrongpassword')
            self.stdout.write(self.style.SUCCESS('processo de criação de Super User Finalizado'))

    def handle(self, *args, **options):
        self.create_super_user()

        self.insert_imoveis()

        self.insert_anuncios()

        self.insert_reservas()
