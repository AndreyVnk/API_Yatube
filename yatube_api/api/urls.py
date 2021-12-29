from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    CommentViewSet,
    PostViewSet,
    GroupViewSet,
    FollowViewSet,
    CreateUserViewSet
)

router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet)
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comment')
router_v1.register('group', GroupViewSet)
router_v1.register('follow', FollowViewSet, basename='follow')
router_v1.register('auth', CreateUserViewSet, basename='auth')


api_patterns_v1 = [
    path('token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('', include(router_v1.urls)),
]

urlpatterns = [
    path('v1/', include(api_patterns_v1)),
]
