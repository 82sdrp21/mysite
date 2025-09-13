from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView
from blog.models import Post, Category
from django.http import Http404

class BlogListView(ListView):

    template_name = 'blog/blog-list.html'
    model = Post
    queryset = Post.objects.filter(status=1)
    context_object_name = 'posts'
    paginate_by = 2
    

class CategoryListView(BlogListView):
    
    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(categories__name=self.kwargs.get('cat'), status=1)
        

class AuthorListView(BlogListView):
    
    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(author__username__exact=self.kwargs.get('username'), status=1)
    
class SearchListView(BlogListView):

    def get_queryset(self, *args, **kwargs):

        if search_word := self.request.GET.get('s'):
            posts = Post.objects.filter(title__icontains=search_word, content__icontains=search_word, status=1)
            return posts
        else:
            raise Http404
        
class TagsListView(BlogListView):

    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(tags__name__in=[self.kwargs.get('tag')])


class BlogDetailView(DetailView):
    template_name = 'blog/blog-detail.html'
    model = Post
    context_object_name = 'post'
