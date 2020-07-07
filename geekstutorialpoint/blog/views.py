from django.shortcuts import render
from .models import Post,Comment
from . import serializers
from rest_framework import generics,status
from rest_framework.response import Response


# Get Requests 
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    seriealizer_class = serializers.CommentSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

