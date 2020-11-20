from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User


# relationships
# we'd like to use a hyperlinked style between entities. In order to do so, we'll modify our serializers, extending HyperlinkedModelSerializer
# The HyperlinkedModelSerializer has the following differences from ModelSerializer:

# It does not include the id field by default.
# It includes a url field, using HyperlinkedIdentityField.
# Relationships use HyperlinkedRelatedField, instead of PrimaryKeyRelatedField.


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    # we also need to indicate on the highlight field that any format suffixed hyperlinks it returns should use the '.html' suffix.
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight',
                  'title', 'code', 'linenos', 'language', 'style',
                  'owner']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True,
                                                   view_name='snippet-detail',
                                                   read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']

