# Generated by Django 4.2.9 on 2024-06-07 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bid",
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
                ("fio", models.CharField(max_length=255, verbose_name="ФИО")),
                ("user_id", models.PositiveIntegerField(verbose_name="id отправителя")),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("type_problem", models.CharField(max_length=255)),
                ("problem", models.CharField(max_length=255)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("CD", "CREATED"),
                            ("PR", "PROCESSING"),
                            ("PD", "PASSED"),
                        ],
                        max_length=2,
                    ),
                ),
            ],
            options={
                "verbose_name": "заявка",
                "verbose_name_plural": "заявки",
            },
        ),
    ]
