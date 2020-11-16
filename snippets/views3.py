from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import mixins, generics
# The create/retrieve/update/delete operations that we've been using so far are going to be pretty similar for any model-backed API views we create.
# Those bits of common behaviour are implemented in REST framework's mixin classes.

# ref) https://velog.io/@jcinsh/RetrieveUpdateDestroyView-%EC%9D%B4%ED%95%B4
# DetailAPIView인데 왜 queryset은 Customer.objects.all()인가?
# 코드는 아주 심플한테, 어떻게 이 3줄의 코드가 detail, update, delete 기능을 수행하는가?
# Mixin 과 GenericAPIView 상속, 각 request method 에 대한 연결을 해주고 있기 때문


class SnippetList(generics.ListCreateAPIView):
    """
    List all snippets, or create a new snippet.
    REST framework provides a set of already mixed-in generic views
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


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
