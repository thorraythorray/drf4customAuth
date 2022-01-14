from django.urls import path

from apps.docker_scan.views import Test

urlpatterns = [
    path('test/', Test.as_view())
]
