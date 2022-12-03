from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'api/v1/posts', PostViewSet)
router.register(r'api/v1/posts/(?P<id>[0-9]+)/comments', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]