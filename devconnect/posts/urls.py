from django.urls import path
from .views import PostListView, PostCreateView, PostDetailView, CommentCreateView

urlpatterns = [
    path('', PostListView.as_view()),
    path('create/', PostCreateView.as_view()),
    path('<int:pk>/', PostDetailView.as_view()),
    path('comments/create/', CommentCreateView.as_view()),
]