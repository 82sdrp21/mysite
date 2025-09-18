from django.contrib.syndication.views import Feed
from blog.models import Post

class LatestPostFeed(Feed):
    title = "Travel's lestest blog posts"
    link = '/feed/'
    description = 'Do not fool yourself'

    def item(self):
        return Post.objects.all()
    
    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        return item.content

