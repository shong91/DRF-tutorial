from django.urls import path, include
from boards import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'board', views.BoardViewSet)
router.register(r'comment', views.CommentViewSet)
router.register(r'view/comment', views.CommentOnlyViewSet)

urlpatterns = [
    path('', include(router.urls))
]
