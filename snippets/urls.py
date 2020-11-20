from django.urls import path, include
# from snippets import views, views2, views3, views4, views5
from snippets.views6_viewset import UserViewSet, SnippetViewSet
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from snippets import views6_viewset

# function based view urlpattern
# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail)
# ]

# class based view urlpatterns
# as_view() 함수는 클래스의 인스턴스를 생성하고, 인스턴스의 dispatch() 메소드를 호출한다.
# dispatch() 메소드는 요청을 검사해서 GET, POST 등의 어떤 HTTP 메소드로 요청되었는지 알아낸 다음, 인스턴스 내에서 해당 이름을 갖는 메소드로 요청을 중계해준다.
# 만일 해당 메소드가 정의되어 있지 않으면 HttpResponseNotAllowed 익셉션을 발생시킵니다.

# hyperlinked API 사용하기 ==============================================================================================
# we need to make sure we name our URL patterns. (The root of our API refers to 'user-list' and 'snippet-list')
# urlpatterns = [
#     path('', views5.api_root),
#
#     path('snippets/', views5.SnippetList.as_view(), name='snippet-list'),
#     path('snippets/<int:pk>/', views5.SnippetDetail.as_view(), name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/', views5.SnippetHighlight.as_view(), name='snippet-highlight'),
#
#     path('users/', views5.UserList.as_view(), name='user-list'),
#     path('user/<int:pk>', views5.UserDetail.as_view(), name='user-detail'),
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)

# Format Suffixes
# URL에서 파일 이름 확장자를 사용하여 특정 미디어 유형에 대한 엔드포인트를 제공 ex)‘http://example.com/api/users.json’
# format_suffix_patterns: 제공된 각 URL 패턴에 추가 된 형식 접미사 패턴을 포함하는 URL 패턴 list를 반환
# 각 view 에 format 인자를 추가 (format=None)
# => format_suffix_patterns 를 통해 특정 포맷을 간단하고 명확하게 참조할 수 있다.

# ViewSet 사용하기 (binding ViewSet) ====================================================================================
snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get': 'list'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

# urlpatterns = format_suffix_patterns([
#     path('', api_root),
#     path('snippets/', snippet_list, name='snippet-list'),
#     path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
#
#     path('users/', user_list, name='user-list'),
#     path('user/<int:pk>', user_detail, name='user-detail'),
# ])

# Router 사용하기 ======================================================================================================
# Create a router and register our viewsets with it.
# The conventions for wiring up resources into views and urls can be handled automatically, using a Router class
# The DefaultRouter class we're using also automatically creates the API root view for us, so we can now delete the api_root method from our views module.

router = DefaultRouter()
router.register(r'snippets', views6_viewset.SnippetViewSet)
router.register(r'users', views6_viewset.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

