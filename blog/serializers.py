from rest_framework import serializers

from .models import Post, Review


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('slug', 'author', 'title', 'description', 'content', 'created_at', 'updated_at')
        model = Post
