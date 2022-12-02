from rest_framework import serializers

from posts.models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username", read_only=True)
    class Meta():
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'image')
