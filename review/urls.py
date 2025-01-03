from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ReviewViewset

router = DefaultRouter()

router.register('', ReviewViewset)

urlpatterns = [
    path('', include(router.urls)),
]