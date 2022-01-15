from django.urls import path, include

from apps.vul_scan import views
from proj.urls import router


router.register(r'tasks', views.ScanTaskViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
