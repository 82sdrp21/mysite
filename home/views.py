from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from home.models import NewsLetter
from django.contrib.messages.views import SuccessMessageMixin
from blog.models import Post
from home.forms import ContactForm

class IndexView(TemplateView):
    template_name = 'home/index.html'
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['posts'] = Post.objects.filter(status=1).order_by('-updated_date')[:4]

        return context

class AboutView(TemplateView):
    template_name = 'home/about.html'

class ContactView(SuccessMessageMixin, CreateView):
    template_name = 'home/contact.html'
    form_class = ContactForm
    # fields = ['name', 'email', 'subject', 'message', 'captcha',]
    success_url = reverse_lazy('home:contact_page')
    success_message = 'Your ticket is successfully submitted!'
    

class NewsLetterView(CreateView):
    model = NewsLetter
    fields = ['email']
    success_url = reverse_lazy('home:home_page')

