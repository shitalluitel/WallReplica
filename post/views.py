from django.shortcuts import render, redirect
from post.forms import PostForm
from django.urls import reverse
from post.models import Post

# Create your views here.


def create_post(request, *args, **kwargs):
    method = request.method.lower()
    if method == 'get':
        form = PostForm()
    elif method == 'post':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('post:list'))

    return render(
        request=request,
        template_name='post/create.html',
        context={'form': form}
    )


def list_post(request, *args, **kwargs):
    posts = Post.objects.all()
    form = PostForm()
    
    return render(
        request=request,
        template_name='post/create.html',
        context={
            'posts': posts,
            'form': form
        }
    )
