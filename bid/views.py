import rest_framework.views
import rest_framework.status
import rest_framework.response

import bid.serializers
import bid.models


class BidViewSet(rest_framework.views.APIView):

    queryset = bid.models.Bid.objects.all()
    serializer_class = bid.serializers.BidSerializer

    def post(self, request):
        serializer = bid.serializers.BidSerializer(
            data=request.data,
        )
        if serializer.is_valid():
            serializer.save()
            return rest_framework.response.Response(
                serializer.data,
                status=rest_framework.status.HTTP_201_CREATED,
            )

        return rest_framework.response.Response(
            serializer.errors,
            status=rest_framework.status.HTTP_400_BAD_REQUEST,
        )
