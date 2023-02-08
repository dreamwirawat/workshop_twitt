
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib    import messages
from django.http import HttpRequest,HttpResponseRedirect
from django.contrib.auth import logout


from .forms import PostForm


# import models
from app_post.models import Post,Sex,Post,Tag,PostTag 



# Create your views here.
#home
@login_required
def home(request):
    posts=Post.objects.all().order_by('-date_time')
    sex=Sex.objects.all()
    trends=Tag.objects.all().order_by('-value')[:5]
    PostTags = PostTag.objects.all()
    return render (request,"homes/home.html",{
        'posts':posts,
        'sex':sex,
        'PostTags':PostTags,
        'trends':trends
    })


def create_post(request):
    if request.method == 'POST': 
        if request.user.is_authenticated:  
            author = request.user
        else:
           return redirect('../../home/')
        post = request.POST['newpost']
        tag=request.POST['tag']
        new_post = Post.objects.create(
            content=post,
            user=author,
        )
        tag_obj, created = Tag.objects.get_or_create(
            tag_content=tag,
            defaults={'value': 1}
        )
        if not created:
            tag_obj.value += 1
            tag_obj.save()
        new_post.id_tag.add(tag_obj)
        return redirect('../../home/')






  