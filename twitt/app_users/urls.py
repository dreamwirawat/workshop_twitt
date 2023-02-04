from django.urls import path,include
from . import views

urlpatterns = [
 

  path('',include("django.contrib.auth.urls")),

  path('',views.ToExplore, name="ToExplore" ),

  path('',views.addUser),

  path('addUser',views.addUser),
  
  path('logout/', views.logout_view, name='logout'),
  
  

]
