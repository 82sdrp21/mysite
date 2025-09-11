from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from home.models import Contact, NewsLetter
from django.contrib.messages.views import SuccessMessageMixin

class IndexView(TemplateView):
    template_name = 'home/index.html'

class AboutView(TemplateView):
    template_name = 'home/about.html'

class ContactView(SuccessMessageMixin, CreateView):
    template_name = 'home/contact.html'
    model = Contact
    fields = ['name', 'email', 'subject', 'message',]
    success_url = reverse_lazy('home:contact_page')
    success_message = 'Your ticket is successfully submitted!'
    

class NewsLetterView(CreateView):
    model = NewsLetter
    fields = ['email']
    success_url = reverse_lazy('home:home_page')

