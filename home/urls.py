from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home_page'),
    path('contact', views.ContactView.as_view(), name='contact_page'),
    path('about', views.AboutView.as_view(), name='about_page'),
]
