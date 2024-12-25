from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import AccountViewset, RegistrationApiView, LoginApiView, LogoutApiView

router = DefaultRouter()

router.register('', AccountViewset)

urlpatterns = [
    path('list/', include(router.urls)),
    path('register/', RegistrationApiView.as_view(), name='register'),
    path('login/', LoginApiView.as_view(), name='login'),
    path('logout/', LogoutApiView.as_view(), name='logout'),
]