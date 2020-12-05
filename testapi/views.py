from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .task import send_email


@api_view(['GET'])
@permission_classes([AllowAny])
def send_test_email(request):
    # celery로 작업하고 싶은 작업은 delay()를 붙여줘야 합니다.
    send_email.delay()
    return Response({'message': 'ok'})


# @api_view(['GET'])
# @permission_classes([AllowAny])
# def send_test_email(request):
#     subject = "이메일 테스트2"
#     to = ['hhhongso@gmail.com']
#     message = "email test가 성공했습니다."
#     EmailMessage(subject=subject, body=message, to=to, from_email=FROM_EMAIL).send()
#
#     return Response({"message": "ok"})

# 다만 이런 방식은 api 시간이 오래 걸리는 문제점이 있습니다. 해당 test도 5초가 소모되었습니다.
# => 해결법: redis, celery
# 1. Celery ?
# 비동기 작업을 위한 파이썬 프레임워크
# 2. Redis ? (AWS)
# Remote Dictionary Server. 메모리 키 값 데이터 구조 스토어.
# 다양한 인 메모리 데이터 구조 집합을 제공하여 사용자 정의 애플리케이션을 생성할 수 있다.
