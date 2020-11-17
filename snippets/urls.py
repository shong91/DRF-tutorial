from django.urls import path
from snippets import views, views2, views3, views4
from rest_framework.urlpatterns import format_suffix_patterns

# function based view urlpattern
# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail)
# ]

# class based view urlpatterns
# as_view() 함수는 클래스의 인스턴스를 생성하고, 인스턴스의 dispatch() 메소드를 호출한다.
# dispatch() 메소드는 요청을 검사해서 GET, POST 등의 어떤 HTTP 메소드로 요청되었는지 알아낸 다음, 인스턴스 내에서 해당 이름을 갖는 메소드로 요청을 중계해준다.
# 만일 해당 메소드가 정의되어 있지 않으면 HttpResponseNotAllowed 익셉션을 발생시킵니다.

urlpatterns = [
    path('snippets/', views4.SnippetList.as_view()),
    path('snippets/<int:pk>/', views4.SnippetDetail.as_view()),

    path('users/', views4.UserList.as_view()),
    path('user/<int:pk>', views4.UserDetail_as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)

# Format Suffixes
# URL에서 파일 이름 확장자를 사용하여 특정 미디어 유형에 대한 엔드포인트를 제공 ex)‘http://example.com/api/users.json’
# format_suffix_patterns: 제공된 각 URL 패턴에 추가 된 형식 접미사 패턴을 포함하는 URL 패턴 list를 반환
# 각 view 에 format 인자를 추가 (format=None)
# => format_suffix_patterns 를 통해 특정 포맷을 간단하고 명확하게 참조할 수 있다.
