from django.urls import path
from .views import FollowUserView, UserListView, RegisterView

urlpatterns = [
    path('follow/', FollowUserView.as_view()),
    path('register/', RegisterView.as_view()),
    path('', UserListView.as_view()),
    
]