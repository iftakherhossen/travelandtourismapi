from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TeamViewset

router = DefaultRouter()

router.register('', TeamViewset)

urlpatterns = [
    path('list/', include(router.urls)),
]