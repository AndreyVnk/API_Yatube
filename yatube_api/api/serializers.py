from rest_framework import serializers
from django.core.exceptions import ValidationError

from .models import Comment, Group, Post, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'pub_date')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('title',)


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
    )

    class Meta:
        model = Follow
        fields = ('user', 'following',)

    def validate(self, attrs):
        if self.context['request'].user == attrs['following']:
            raise ValidationError('You can`t subscribe to yourself')
        if Follow.objects.filter(user=self.context['request'].user,
                                 following=attrs['following']).exists():
            raise ValidationError('You have already subscribed to this user')
        return super().validate(attrs)
