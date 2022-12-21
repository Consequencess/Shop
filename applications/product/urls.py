from django.urls import include, path
from rest_framework.routers import DefaultRouter

from applications.product.views import ProductAPIView, CategoryAPIView

router = DefaultRouter()
router.register('category', CategoryAPIView)
router.register('', ProductAPIView)
urlpatterns = [
    path('', include(router.urls))
]
