from rest_framework import serializers
from boards.models import Board, Comment


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'author', 'title', 'body', 'created_at', 'updated_at']
    author = serializers.ReadOnlyField(source='author.username')

    def create(self, validated_data):
        return Board.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.language = validated_data.get('language', instance.language)
        instance.save()
        return instance


class CommentSerializer(serializers.ModelSerializer):
    reply = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['board', 'id', 'user', 'parent', 'comment', 'created_at', 'reply']
        read_only_fields = ['user']

    # 댓글이 있을 경우, 대댓글 데이터를 가져온다.
    def get_reply(self, instance):
        serializer = self.__class__(instance.reply, many=True)
        serializer.bind('', self)
        return serializer.data


class BoardOnlySerializer(serializers.ModelSerializer):
    parent_comments = serializers.SerializerMethodField()
    class Meta:
        model = Board
        fields = ('id', 'parent_comments')

    def get_parent_comments(self, instance):
        parent_comments = instance.comments.filter(parent=None) # filter: 대댓글이 아닌 원댓글
        serializer = CommentSerializer(parent_comments, many=True) # model 을 Board 로 설정하여, 게시글에 맞는 원댓글 값을 가져온다.
        return serializer.data

# Practice for SerializerMethodField: 커스텀 필드 만들기
# SerializerMethodField 는 조회할 때 사용하는데, (저장, 수정 X)
# 인자로 method_name 으로 해당 필드값에 대해 정의하는 함수의 이름을 넘겨주며,
# 지정하지 않을 경우 default = get_<field_name> 으로 지정할 수 있다.
class ReviewSerializer(serializers.ModelSerializer):
    # Review 모델은 Profile 모델과 FK 연결되어 있으며, profile의 id 값으로 사용자의 이름을 추가적으로 가져오려한다.
    username = serializers.SerializerMethodField()

    class Meta:
        # model = Review
        # serializer 로 조회 시 username 도 return 받을 수 있도록 필드에 추가한다.
        fields = ['username', 'profile', 'content', 'created_at']

    # method_name default = get_<field_name>
    def get_username(self, instance):
        return instance.profile.nickname