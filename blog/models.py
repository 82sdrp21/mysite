from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='media', blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='posts')
    views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(editable=False, null=True, blank=True)

    class Meta:
        ordering = ['-updated_date']
        verbose_name = 'Post'
        verbose_name_plural = 'Blog'


    def __str__(self):
        return f"{self.title}: {self.author.username}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(args, kwargs)

