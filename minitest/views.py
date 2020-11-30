from django.shortcuts import render
from rest_framework import viewsets
from minitest.serializer import UserSerializer, BoardSerializer
from django.contrib.auth.models import User
from minitest.models import Board

from minitest.permissions import IsOwnerOrReadOnly
from rest_framework import permissions, renderers

from rest_framework.decorators import action
from rest_framework.response import Response

# ViewSet: 일반적인 CBV 가 아니기 때문에 as_view 를 통해서 뷰를 만들지 않고 router를 사용했습니다.
# as_view 를 사용하지 않는 이유는 ViewSet 은 하나의 뷰가 아닌 set, 여러 개의 뷰를 만들 수 있는 확장된 CBV이기 때문입니다.
#
# ViewSet 은 두 가지 종류로 이루어져 있습니다. 두 종류 모두 자체적인 구현은 없고 Mixin 을 적절히 상속받아 여러 기능을 수행하게 됩니다.
# viewsets.ReadOnlyModelViewSet
# viewsets.ModelViewSet


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *arg, **kwargs):
        board = self.get_object()
        return Response("@action custom")

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)