from django.urls import path, include
from minitest import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'board', views.BoardViewSet)

urlpatterns = [
    path('', include(router.urls))
]