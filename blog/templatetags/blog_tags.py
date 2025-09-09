from django import template
from blog.models import Category, Post

register = template.Library()

@register.inclusion_tag('blog/side-bar.html')
def side_bar():
    cats = Category.objects.all()
    pop_posts = Post.objects.filter(status=True).order_by('-updated_date')[:3]
    return {'categories_collection': cats,'pop_posts': pop_posts,}


