# Generated by Django 4.1 on 2022-11-21 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("labSoft3", "0008_delete_reserva"),
    ]

    operations = [
        migrations.CreateModel(
            name="reserva",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("id_reserva", models.CharField(max_length=200)),
                ("numero_mesa", models.IntegerField()),
                ("tipo_reserva", models.CharField(max_length=200)),
                ("nombre_cliente", models.CharField(max_length=200)),
                ("fecha", models.CharField(max_length=200)),
                ("hora", models.CharField(max_length=200)),
            ],
        ),
    ]
