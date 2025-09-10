from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog-list'),
    path('cat/<str:cat>', views.CategoryListView.as_view(), name='blog-list'),
    path('<slug:slug>', views.BlogDetailView.as_view(), name='blog-detail'),
]
