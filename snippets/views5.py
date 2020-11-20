from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics, permissions, renderers
from django.contrib.auth.models import User
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


# Create a single entry point to our API, by using Function based view
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })


# we don't want to use JSON, but instead just present an HTML representation.
# There are two styles of HTML renderer provided by REST framework,
# one for dealing with HTML rendered using templates, the other for dealing with pre-rendered HTML.
class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)


# read-only views
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# read and create views (authentication & permissions)
class SnippetList(generics.ListCreateAPIView):
    """
    List all snippets, or create a new snippet.
    REST framework provides a set of already mixed-in generic views
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # 권한 종류
    # IsAuthenticatedOrReadOnly 인증된 사용자에게는 허용하고 그렇지 않은 사용자는 읽기만 가능
    # IsAuthenticated 인증된 사용자에게만 허용
    # IsAdminUser 관리자에게만 허용
    # AllowAny 모두 허용

    # The way we deal with that is by overriding a .perform_create() method on our snippet views.
    # 로그인 한 채로 POST요청을 보낼 때 테이블의 외래키 필드를 유저 모델과 자동으로 연결시킨다.
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    # the defaults [SessionAuthentication and BasicAuthentication] are currently applied.
    # When we interact with the API through the web browser, we can login, and the browser session will then provide the required authentication for the requests.
    # If we're interacting with the API programmatically we need to explicitly provide the authentication credentials on each request.


# 참조: 함수기반 뷰에서의 권한 지정 - 데코레이터 사용
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def 함수():
#     pass


# class SnippetList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     """
#     List all snippets, or create a new snippet.
#     - mixin classes provide the .list() and .create() actions. We're then explicitly binding the get and post methods to the appropriate action
#     - GenericAPIView class to provide the core functionality,
#     """
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
