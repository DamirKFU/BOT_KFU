import django.db.models


class Bid(django.db.models.Model):
    CHOICES = (
        ("CD", "Создано"),
        ("PR", "В процессе"),
        ("PD", "Завершено"),
    )
    fio = django.db.models.CharField(
        "ФИО",
        max_length=255,
    )
    user_id = django.db.models.PositiveIntegerField(
        "id отправителя",
    )
    created = django.db.models.DateTimeField(
        "создано",
        auto_now_add=True,
    )
    updated = django.db.models.DateTimeField(
        "обновлено",
        auto_now=True,
    )
    type_problem = django.db.models.CharField(
        "тип проблемы",
        max_length=255,
    )
    problem = django.db.models.CharField(
        "проблема",
        max_length=255,
    )
    status = django.db.models.CharField(
        "статус",
        choices=CHOICES,
        default=CHOICES[0][0],
        max_length=2,
    )

    class Meta:
        verbose_name = "заявка"
        verbose_name_plural = "заявки"
