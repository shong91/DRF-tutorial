from rest_framework import serializers
from django.contrib.auth.models import User
from minitest.models import Board


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'board']
    board = serializers.PrimaryKeyRelatedField(many=True,
                                               queryset=Board.objects.all())


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'owner', 'title', 'code', 'language']
    owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        return Board.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.language = validated_data.get('language', instance.language)
        instance.save()
        return instance
