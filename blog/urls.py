from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog-list'),
    path('cat/<str:cat>', views.CategoryListView.as_view(), name='blog-list-category-filtered'),
    path('author/<str:username>', views.AuthorListView.as_view(), name='blog-list-author-filtered'),
    path('search', views.SearchListView.as_view(), name='blog-list-search'),
    path('<slug:slug>', views.BlogDetailView.as_view(), name='blog-detail'),
]
