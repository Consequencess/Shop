from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.feedback.views import CommentAPIView, FavoriteAPIView

router = DefaultRouter()
router.register('comment', CommentAPIView)
router.register('favorite', FavoriteAPIView)

urlpatterns = [
    path('', include(router.urls))
]