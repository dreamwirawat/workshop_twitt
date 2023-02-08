from django.urls import path,include
from . import views

urlpatterns = [
 

  path('',views.home , name="home" ),
  path('post',views.create_post ),

  path('post_data',views.create_post,name="create_post"),
 


]