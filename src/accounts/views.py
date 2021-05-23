from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.views.generic import DetailView, TemplateView
from django.views.generic.base import View
from django.views.generic.edit import UpdateView
from accounts.models import UserProfile

from accounts.forms import UserLoginForm, UserRegistrationForm, ProfileForm


class ProfileDetailView(TemplateView):
    model = UserProfile
    template_name = "accounts/detail.html"



def login_view(request):
    form = UserLoginForm(request.POST or None)
    _next = request.GET.get('next')
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        _next = _next or '/'
        return redirect(_next)
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def registration_view(request):
    # if request.method == "POST":
    #     form = UserRegistrationForm(request.POST)
    #     if form.is_valid():
    #         new_user = form.save(commit=False)
    #         new_user.set_password(form.cleaned_data['password'])
    #         new_user.save()
    #         return render(request, 'accounts/register_done.html', {'new_user': new_user})
    #     return render(request, 'accounts/register.html', { 'form': form })
    # else:
    #     form = UserRegistrationForm()
    #     return render(request, 'accounts/register.html', { 'form': form })
    
    if request.method == "POST":
        u_form = UserRegistrationForm(request.POST)
        p_form = ProfileForm(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            print('is valid')
            user = u_form.save(commit=False)
            user.set_password(u_form.cleaned_data['password'])
            user.save()
            p_form = p_form.save(commit=False)
            p_form.user = user
            p_form.save()
            print(user, p_form)
            return redirect('accounts:login')
    else:
        u_form = UserRegistrationForm(request.POST)
        p_form = ProfileForm(request.POST)
    return render(request, 'accounts/register.html', {'u_form': u_form, 'p_form': p_form})

