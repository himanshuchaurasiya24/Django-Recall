from django.shortcuts import render
from rest_framework import generics, viewsets
from blog.models import *
from blog.serializers import *
from rest_framework.filters import SearchFilter,OrderingFilter

# Create your views here.

class BlogModelViewSet(viewsets.ModelViewSet):
    queryset= Blog.objects.all()
    serializer_class= BlogSerializer
    filter_backends= [SearchFilter, OrderingFilter]
    # filter_backends= [ OrderingFilter]
    search_fields= ['blog_title', 'blog_body']  # Specify the fields to search on
    # search_fields= ['^blog_title', 'blog_body']  # The ^ symbol is to search the given word in the sentence which start with it, Specify the fields to search on
    ordering_fields= ['blog_title', 'blog_body','id']  # Specify the fields to order by
    # lookup_field = 'blog_title'  # Specify the lookup field for the Blog model
class CommentModelViewSet(viewsets.ModelViewSet):
    queryset= Comment.objects.all()
    serializer_class= CommentSerializer
    filter_backends= [SearchFilter]
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