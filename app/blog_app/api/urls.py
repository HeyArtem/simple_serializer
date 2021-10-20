from django.urls import path
from blog_app.views import (blog_post_list,
                            BlogPostList
                            )                            

urlpatterns = [
    # активация сериалайзера через функцию
    path('', blog_post_list),
    # активация сериалайзера через класс
    path('сlass/', BlogPostList.as_view())
]
