from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
# Format Suffixes
# URL에서 파일 이름 확장자를 사용하여 특정 미디어 유형에 대한 엔드포인트를 제공 ex)‘http://example.com/api/users.json’
# format_suffix_patterns: 제공된 각 URL 패턴에 추가 된 형식 접미사 패턴을 포함하는 URL 패턴 list를 반환
# 각 view 에 format 인자를 추가 (format=None)
# => format_suffix_patterns 를 통해 특정 포맷을 간단하고 명확하게 참조할 수 있다. 
