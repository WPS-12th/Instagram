from rest_framework import serializers

from members.serializers import UserSerializer
from .models import Post, PostImage, PostComment


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = (
            'pk',
            'image',
        )


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    postimage_set = PostImageSerializer(many=True)

    class Meta:
        model = Post
        fields = (
            'pk',
            'author',
            'content',
            'postimage_set',
        )


class PostCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField()
    )

    class Meta:
        model = Post
        fields = (
            'images',
            'content',
        )

    def create(self, validated_data):
        images = validated_data.pop('images')
        post = super().create(validated_data)
        for image in images:
            serializer = PostImageCreateSerializer(data={'image': image})
            if serializer.is_valid():
                serializer.save(post=post)
        return post

    def to_representation(self, instance):
        return PostSerializer(instance).data


class PostImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = (
            'image',
        )


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = (
            'pk',
            'content',
        )


class PostCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = (
            'content',
        )

    def to_representation(self, instance):
        return PostCommentSerializer(instance).data
