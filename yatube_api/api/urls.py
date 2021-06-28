from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import CommentViewSet, PostViewSet, GroupViewSet, FollowViewSet

router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet)
router_v1.register(r'posts/(?P<post_id>[^/.]+)/comments',
                   CommentViewSet, basename='comment')
router_v1.register('group', GroupViewSet)
router_v1.register('follow', FollowViewSet, basename='follow')


api_patterns_v1 = [
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/', include(router_v1.urls)),
]

urlpatterns = [
    path('api/', include(api_patterns_v1)),
]
