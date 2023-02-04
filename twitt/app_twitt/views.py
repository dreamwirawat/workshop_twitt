from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib    import messages
from django.http import HttpRequest,HttpResponseRedirect
from django.contrib.auth import logout


# Create your views here.
#home
def home(request):
    return render (request,"general/home.html")



