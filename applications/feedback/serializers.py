from rest_framework import serializers
from applications.feedback.models import Comment, Favorite, Like, Rating


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)

    class Meta:
        model = Comment
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)

    class Meta:
        model = Favorite
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    # rating = serializers.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Rating
        fields = ['rating']
