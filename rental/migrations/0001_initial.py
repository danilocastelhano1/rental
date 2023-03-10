# Generated by Django 4.1.5 on 2023-01-05 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('nome_plataforma', models.CharField(max_length=150)),
                ('taxa_plataforma', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
            options={
                'verbose_name_plural': 'Anúncios',
            },
        ),
        migrations.CreateModel(
            name='Imoveis',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('hospedes_limite', models.PositiveIntegerField()),
                ('qtde_banheiros', models.PositiveIntegerField()),
                ('pet_friendly', models.BooleanField(default=False)),
                ('valor_limpeza', models.DecimalField(decimal_places=2, max_digits=12)),
                ('data_ativacao', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Imóveis',
            },
        ),
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('data_check_in', models.DateField()),
                ('data_check_out', models.DateField()),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=12)),
                ('comentarios', models.TextField()),
                ('qtde_hospedes', models.PositiveIntegerField()),
                ('anuncio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserva', to='rental.anuncios')),
            ],
            options={
                'verbose_name_plural': 'Reservas',
            },
        ),
        migrations.AddField(
            model_name='anuncios',
            name='imovel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anuncio', to='rental.imoveis'),
        ),
    ]
