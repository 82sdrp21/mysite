from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['home:home_page','home:about_page','home:contact_page',]
    
    def location(self, item):
        return reverse(item)


