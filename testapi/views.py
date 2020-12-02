from django.core.mail.message import EmailMessage
from DRFtutorial import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

FROM_EMAIL = settings.EMAIL_HOST_USER


@api_view(['GET'])
@permission_classes([AllowAny])
def send_test_email(request):
    subject = "이메일 테스트2"
    to = ['hhhongso@gmail.com']
    message = "email test가 성공했습니다."
    EmailMessage(subject=subject, body=message, to=to, from_email=FROM_EMAIL).send()

    return Response({"message": "ok"})

# 다만 이런 방식은 api 시간이 오래 걸리는 문제점이 있습니다. 해당 test도 5초가 소모되었습니다.
# 다음 포스트에서는 이 문제점을 해결하는 여러가지 방법이 있겠지만 Fit-ple 프로젝트에서 진행한 방법에 대해 작성하겠습니다.
# 이어하기: https://velog.io/@lemontech119/DRF%EB%A1%9C-api-%EC%84%9C%EB%B2%84-%EA%B0%9C%EB%B0%9C6-celery