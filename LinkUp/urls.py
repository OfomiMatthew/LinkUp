from django.urls import path 
from . import views

urlpatterns = [
   path('',views.home,name='home'),
   path('sign-up',views.sign_up,name='sign-up'),
  path('login',views.log_in,name='login'),
  path('logout',views.log_out,name='logout'),
  path('upload',views.upload,name='upload'),
  path('like-post/<str:id>/',views.like_post,name='like-post'),
  path('#<str:id>',views.detail_post,name='detail-post'),
  path('explore',views.explore,name='explore'),
  path('profile/<str:id_user>/',views.profile,name='profile'),
  path('follow',views.follow,name='follow'),
  path('delete/<str:id>',views.delete_post,name='delete-post'),
  path('search/',views.search_result,name='search')
   
]
