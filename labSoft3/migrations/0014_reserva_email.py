# Generated by Django 4.1 on 2022-11-21 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("labSoft3", "0013_reserva_numero_personas_reserva_telefono_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="reserva",
            name="email",
            field=models.EmailField(
                max_length=244, null=True, unique=True, verbose_name="email address"
            ),
        ),
    ]