from rest_framework import viewsets
from snippets.serializers_hyperlinked import SnippetSerializer, UserSerializer
from django.contrib.auth.models import User
from snippets.permissions import IsOwnerOrReadOnly
from snippets.models import Snippet
from rest_framework import permissions, renderers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
# ViewSet classes provide operations such as retrieve, or update, and not method handlers such as get or put.
# A ViewSet class is only bound to a set of method handlers at the last moment,
# when it is instantiated into a set of views, typically by using a Router class which handles the complexities of defining the URL conf for you.


# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format),
#         'snippets': reverse('snippet-list', request=request, format=format)
#     })


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    기존의 UserList, UserDetail 클래스를 UserViewSet 으로 통합.
    we no longer need to provide the same information to two separate classes.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    # @action decorator will respond to GET requests by default. (if POST, add argument [method=POST])
    # This decorator can be used to add any custom endpoints that don't fit into the standard create/update/delete style.
    # url default = method name itself. if you want to change, include [url_path] as a decorator keyword argument
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)