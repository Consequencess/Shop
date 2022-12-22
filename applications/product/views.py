from django.shortcuts import render
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from applications.feedback.models import Like, Favorite, Rating
from applications.feedback.serializers import RatingSerializer
from applications.product.models import Product, Category
from applications.product.serializers import ProductSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class ProductAPIView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'owner']
    search_fields = ['title', 'description']
    ordering_fields = ['id']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    @action(detail=True, methods=['POST'])
    def like(self, request, pk, *args, **kwargs):  # post/id/like/
        like_obj, _ = Like.objects.get_or_create(product_id=pk, owner=request.user)
        like_obj.like = not like_obj.like
        like_obj.save()
        status = 'liked'
        if not like_obj.like:
            status = 'unliked'
        return Response({'status': status})

    @action(detail=True, methods=['POST'])
    def rating(self, request, pk, *args, **kwargs):
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj_rating, _ = Rating.objects.get_or_create(product_id=pk, owner=request.user)
        obj_rating.rating = request.data('rating')
        obj_rating.save()
        return Response(request.data, status=status.HTTP_201_CREATED)


class CategoryAPIView(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


