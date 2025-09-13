from django import template
from blog.models import Category, Post

register = template.Library()

@register.inclusion_tag('blog/side-bar.html')
def side_bar(post=None,page_url=None):

    print(post)
    print(page_url)

    cats = Category.objects.all()
    pop_posts = Post.objects.filter(status=True).order_by('-updated_date')[:3]

    if page_url and post:
        if page_url == 'blog-detail':
            tags = post.tags.all

            print(tags)
            
            data = {
            'categories_collection': cats,
            'pop_posts': pop_posts,
            'tags': tags,
            }

    else:
        data = {
            'categories_collection': cats,
            'pop_posts': pop_posts,
            }

    return data


