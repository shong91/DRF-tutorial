from django.contrib.auth.models import User, Group
from rest_framework import serializers
# HyperlinkedModelSerializer: PK를 리턴하는 게 아니라, 실제 리소스에 접근할 URI를 만들어 리턴함
# ViewSet: 설정을 통한 라우팅 자동 할당, 보통 한 개의 모델에 대한 API 집합체를 적은 코드로 구현할 수 있음


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']