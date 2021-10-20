from django.shortcuts import render
from rest_framework import serializers
from rest_framework.serializers import Serializer
from .models import BlogPost
from blog_app.api.serializer import BlogPostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.generics import get_object_or_404

# реализация сериалайзера через функцию (активация в urls)
@api_view(['GET', 'POST'])

# метод 'GET' возвращает (покеазывает) посты
def blog_post_list(request):
    if request.method == 'GET':
        blog_posts = BlogPost.objects.filter(status='published')
        # blog_posts = BlogPost.objects.all()
        serializer = BlogPostSerializer(blog_posts, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # метод 'POST' создает пост
    elif request.method == 'POST':
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # если не POST и не GET возвращается ошибка
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# реализация сериалайзера через через класс (активация в urls)
class BlogPostList(generics.ListAPIView):
    queryset = BlogPost.objects.filter(status='published')
    serializer_class = BlogPostSerializer

