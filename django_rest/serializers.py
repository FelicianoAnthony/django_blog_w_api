from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Post
        #fields = ('id', 'name', 'date_created', 'date_modified')
        fields = ('id', 'author', 'title', 'text', 'created_date', 'published_date')
        #read_only_fields = ('date_created', 'date_modified')