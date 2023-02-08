from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib    import messages
from django.http import HttpRequest,HttpResponseRedirect
from django.contrib.auth import logout

from app_post.models import Post,Sex,Tag,PostTag

def logout_view(request):
    logout(request)
    return redirect('users/')




# Create your views here.


# ToExplore page
def ToExplore(request):
    posts=Post.objects.all().order_by('-date_time')
    sex=Sex.objects.all()
    trends=Tag.objects.all().order_by('-value')[:3]
    PostTags = PostTag.objects.all()
    return render (request,"registration/login.html",{
        'posts':posts,
        'sex':sex,
        'PostTags':PostTags,
        'trends':trends

    })
   

#home
def home(request):
    return render (request,"register/dashbord.html")

# function Register
def addUser(request):
    username=request.POST['username']
    firstname=request.POST['first_name']
    lastname=request.POST['last_name']
    email=request.POST['email']
    password=request.POST['password']
    repassword=request.POST['password']

    if password == repassword :
        if User.objects.filter(username=username).exists():
                messages.info(request,'Username exists')
                print("Username exists")
                return redirect('../users')
        elif User.objects.filter(email=email).exists():
                print("Email exists")
                messages.info(request,'Email exists')
                return redirect('../users')
        else :
            user=User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=firstname,
                last_name=lastname
            )
            user.save
            return redirect('home')
    else  :
        messages.info(request,'password is not matched')
        return redirect('../users')
    

# login page 
def UserLog(request):
    return render (request,"logUser/index.html")

# function login
def login(request):

    username=request.POST['username']
    password=request.POST['password']

    #check 
    user=auth.authenticate(username=username,password=password)

    if user is not None :
       auth.login(request,user)
       return redirect('home')
    else :
        messages.info(request,'ไม่พบข้อมูล')
        return redirect ('../users')

# function login
def logout_view (request):
    logout(request)
    return redirect('../users')

#SuccessLogin
@login_required
def SuccessLogin(request: HttpRequest):
     return render (request,"frontend/home.html" )



def logout_view(request):
    logout(request)
    return redirect('/users')

