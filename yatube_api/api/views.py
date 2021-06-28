from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, mixins, filters

from .models import Post, Group, Follow
from .permissions import IsAuthorOrReadOnlyPermission
from .serializers import (CommentSerializer, PostSerializer,
                          GroupSerializer, FollowSerializer)


class CreateListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                        mixins.CreateModelMixin):
    pass


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnlyPermission,
                          permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group', ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnlyPermission, ]

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(post=post, author=self.request.user)


class GroupViewSet(CreateListViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class FollowViewSet(CreateListViewSet):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username', 'following__username', ]

    def get_queryset(self):
        return Follow.objects.filter(following=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
