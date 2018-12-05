from django.shortcuts import render
from django.http import HttpResponse
#from .models import website,FormData,Document
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from .filters import UserFilter
from django.conf import settings
from django.core.files.storage import FileSystemStorage
#from .forms import DocumentForm


def index(request):
	#return HttpResponse('Hello Pavan!')
	return render(request, 'index.html', {'title' : 'Home'})