import django.contrib.admin

import bid.models


@django.contrib.admin.register(bid.models.Bid)
class BidAdmin(django.contrib.admin.ModelAdmin):
    fields = []
    list_display = [
        bid.models.Bid.created.field.name,
        bid.models.Bid.problem.field.name,
        bid.models.Bid.status.field.name,
        bid.models.Bid.updated.field.name,
    ]
