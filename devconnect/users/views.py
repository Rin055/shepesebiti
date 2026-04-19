from rest_framework import generics, filters
from django.contrib.auth.models import User
from .serializers import UserSerializer
from .models import Follow
from .serializers import FollowSerializer
from rest_framework.permissions import IsAuthenticated

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    search_fields = ['username', 'profile__skills']


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FollowUserView(generics.CreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(follower=self.request.user)