from django.urls import path
from .views import PostListCreate, PostDetail, CommentListCreate,GetDataCustom

urlpatterns = [
    #branch changes
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('posts/<int:post_pk>/comments/', CommentListCreate.as_view(), name='comment-list-create'),
]
"""
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns += [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
"""