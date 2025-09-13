from django.contrib import sitemaps
from django.urls import reverse
from blog.models import Post


class BlogSitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return Post.objects.filter(status=1)
    
    def lastmod(self, item):
        return item.updated_date
    
    def location(self, item):
        return reverse('blog:blog-detail', kwargs={'slug': item.slug})