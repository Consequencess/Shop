from rest_framework import serializers
from applications.feedback.serializers import LikeSerializer, FavoriteSerializer, RatingSerializer
from applications.product.models import Category, Product, Image


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

    def validate_title(self, title):
        if Category.objects.filter(title=title.lower()).exists():
            raise serializers.ValidationError('Такое название уже существует')
        return title


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)
    images = ProductImageSerializer(many=True, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        product = Product.objects.create(**validated_data)
        files = request.FILES
        list_images = []
        for image in files.getlist('images'):
            list_images.append(Image(product=product, image=image))
        Image.objects.bulk_create(list_images)
        print(list_images)
        return product

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['likes'] = instance.likes.filter(like=True).count()
        rep['ratings'] = instance.ratings.filter(rating=True).count()
        return rep




