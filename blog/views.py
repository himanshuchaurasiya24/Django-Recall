from django.shortcuts import render
from rest_framework import generics, viewsets
from blog.models import *
from blog.serializers import *

# Create your views here.

class BlogModelViewSet(viewsets.ModelViewSet):
    queryset= Blog.objects.all()
    serializer_class= BlogSerializer
    # lookup_field = 'blog_title'  # Specify the lookup field for the Blog model
class CommentModelViewSet(viewsets.ModelViewSet):
    queryset= Comment.objects.all()
    serializer_class= CommentSerializer
    # lookup_field = 'blog_id'  # Specify the lookup field for the Comment model

# class BlogListCreateView(generics.ListCreateAPIView):
#     queryset= Blog.objects.all()
#     serializer_class= BlogSerializer

# class BlogRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset= Blog.objects.all()
#     serializer_class= BlogSerializer


# class CommentListCreateView(generics.ListCreateAPIView):
#     queryset= Comment.objects.all()
#     serializer_class= CommentSerializer

# class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset= Comment.objects.all()
#     serializer_class= CommentSerializer