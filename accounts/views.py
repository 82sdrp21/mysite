from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.urls import reverse



def LoginView(request):
    previous_page_url = request.GET.get('next')
    if request.method == "POST":
        previous_page_url = request.POST.get('next')
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(previous_page_url)

    if request.user.is_authenticated:
        return redirect('home:home_page')

    form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)



def LogoutView(request):
    if request.user.is_authenticated:
        app_name = request.resolver_match.app_name
        url_name = request.resolver_match.url_name
        logout(request)
        return redirect(reverse('home:home_page'))
    else:
        return redirect(reverse('accounts:login'))



def RegisterView(request):
    if not request.user.is_authenticated:

        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("accounts:login")
            else:
                messages.error(request, 'Please try again!')

        form = UserCreationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/register.html', context=context)
    else:
        return redirect('home:home_page')