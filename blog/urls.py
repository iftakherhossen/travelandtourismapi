from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BlogViewset

router = DefaultRouter()

router.register('', BlogViewset)

urlpatterns = [
    path('list/', include(router.urls)),
]