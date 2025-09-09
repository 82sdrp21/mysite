from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post

class BlogListView(ListView):
    template_name = 'blog/blog-list.html'
    model = Post
    queryset = Post.objects.filter(status=True)
    context_object_name = 'posts'

class BlogDetailView(DetailView):
    template_name = 'blog/blog-detail.html'
    model = Post
    context_object_name = 'post'
