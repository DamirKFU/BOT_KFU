import rest_framework.serializers

import bid.models


class BidSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = bid.models.Bid
        fields = [
            bid.models.Bid.fio.field.name,
            bid.models.Bid.type_problem.field.name,
            bid.models.Bid.problem.field.name,
            bid.models.Bid.user_id.field.name,
        ]
