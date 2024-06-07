import django.conf
import django.conf.urls.static
import django.contrib.admin
import django.contrib.auth.urls
import django.urls


urlpatterns = [
    django.urls.path(
        "bidcreated/",
        django.urls.include("bid.urls"),
        name="bid",
    ),
    django.urls.path(
        "",
        django.contrib.admin.site.urls,
    ),
]
