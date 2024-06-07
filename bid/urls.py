import django.urls

import bid.views

app_name = "bid"
urlpatterns = [
    django.urls.path(
        "",
        bid.views.BidViewSet.as_view(),
        name="create",
    )
]
