from django.urls import path,include
from . import views
from .views import logout_view

urlpatterns = [
 

  path('',include("django.contrib.auth.urls")),

  path('',views.ToExplore, name="ToExplore" ),

  path('logout/', logout_view, name='logout'),

  path('',views.addUser),

  path('addUser',views.addUser),
  
  path('logout/', views.logout_view, name='logout'),
  
  
  

]
