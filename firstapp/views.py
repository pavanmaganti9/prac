# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PostForm

from .models import blog_posts

# Create your views here.
def index(request):
	#return HttpResponse('Hello Pavan!')
	return render(request, 'index.html', {'title' : 'Home'})
	
def about(request):
	#return HttpResponse('Hello Pavan!')
	return render(request, 'about.html', {'title' : 'About'})
	
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('signup', {'title' : 'Signup'})
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form,'title' : 'Signup'})
	
def login(request):
	return render(request, 'login.html', {'title' : 'Login'})
	
@login_required(login_url='/login/')
def profile(request):
	return render(request, 'profile.html', {'title' : 'Profile'})
	
	
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    return render(request, 'post_form.html', {'form': form})
	
def post_list(request):
	posts = blog_posts.object.all()
    return render(request, 'post_list.html', {'post': posts})
	
