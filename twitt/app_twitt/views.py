from django.shortcuts import render

# Create your views here.
#home
def home(request):
    return render (request,"app_twitt/home.html")