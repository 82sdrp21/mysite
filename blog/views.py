from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView
from blog.models import Post, Category

class BlogListView(ListView):
    template_name = 'blog/blog-list.html'
    model = Post
    queryset = Post.objects.filter(status=1)
    context_object_name = 'posts'

class CategoryListView(ListView):
    template_name = 'blog/blog-list.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(categories__name=self.kwargs.get('cat'))
        


class BlogDetailView(DetailView):
    template_name = 'blog/blog-detail.html'
    model = Post
    context_object_name = 'post'
