from django.db.models import fields
from rest_framework import serializers
from blog_app.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
        
        # # можно конкретно прописать каие поля сериализовать
        # fields = ('id', 'img', 'description')
        
        # # или сериализовать все кроме
        # exclude =('content')
