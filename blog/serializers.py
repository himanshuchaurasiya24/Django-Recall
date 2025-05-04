from rest_framework import serializers
from blog.models import *

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

        
class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many= True, read_only=True)  # Nested serializer for comments  
    class Meta:
        model = Blog
        fields = '__all__'