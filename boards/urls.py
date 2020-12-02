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

# 이어하기
# https://velog.io/@lemontech119/DRF%EB%A1%9C-api-%EC%84%9C%EB%B2%84-%EA%B0%9C%EB%B0%9C2-%EA%B2%8C%EC%8B%9C%EA%B8%80