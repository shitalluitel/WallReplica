from django.urls import path
from post.views import create_post, list_post

app_name = 'post'

urlpatterns = [
    path('', list_post, name='list'),
    path('create/', create_post, name='create'),
]
