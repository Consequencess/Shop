
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework.viewsets import ModelViewSet

from applications.feedback.models import Comment, Favorite, Like
from applications.feedback.serializers import CommentSerializer, FavoriteSerializer, LikeSerializer


class CommentAPIView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FavoriteAPIView(ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


