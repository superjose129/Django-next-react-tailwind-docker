from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers
from char_count import views
from django.contrib import admin


# Routers provide an easy way of automatically determining the URL conf.
class OptionalSlashRouter(routers.SimpleRouter):
    """Allow the url to have a trailing slash (or not)"""

    def __init__(self):
        super().__init__()
        self.trailing_slash = "/?"


router = OptionalSlashRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("char_count/", views.CharCount.as_view(), name="char_count"),
    path("char_count", views.CharCount.as_view(), name="char_count"),
    path("/", include("rest_framework.urls", namespace="rest_framework")),
    path(r"admin/", admin.site.urls),
]
