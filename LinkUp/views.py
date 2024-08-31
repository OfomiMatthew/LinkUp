from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse
from .models import *
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
  following_users = Follower.objects.filter(follower=request.user.username).values_list('user',flat=True)
  
  post = Post.objects.filter(Q(user=request.user.username) | Q(user__in=following_users)).order_by('-created_at')
  profile = Profile.objects.get(user=request.user)
  
  return render(request,'LinkUp/home.html',{'posts':post,'profile':profile})


def sign_up(request):
  
  try:
    if request.method == 'POST':
      f_name = request.POST.get('f_name')
      email_id = request.POST.get('email_id')
      pass_word = request.POST.get('pass_word')
      my_user = User.objects.create_user(f_name,email_id,pass_word)
      my_user.save()
      # create user profile
      user_model = User.objects.get(username=f_name)
      new_profile = Profile.objects.create(user=user_model,id_user=user_model.id)
      new_profile.save()
      if my_user is not None:
        login(request,my_user)
        return redirect('home')
      return redirect('sign-up')
        
  except:
    invalid = "User Already Exists"
    return render(request,'LinkUp/signup.html',{'invalid':invalid})
  
  return render(request, 'LinkUp/signup.html')

def log_in(request):
  if request.method == 'POST':
    f_name=request.POST.get('f_name')
    pass_word = request.POST.get('pass_word')
    log_user = authenticate(request,username=f_name,password=pass_word)
    if log_user is not None:
      login(request,log_user)
      return redirect('home')
    
    invalid = 'Invalid Credentials'
    return render(request,'LinkUp/login.html',{'invalid':invalid})
  return render(request, 'LinkUp/login.html')

@login_required
def log_out(request):
  logout(request)
  return redirect('login')

@login_required
def upload(request):
  if request.method == 'POST':
    user = request.user.username
    image = request.FILES.get('image-upload')
    caption = request.POST.get('caption')
    new_post = Post.objects.create(user=user,image=image,caption=caption)
    new_post.save()
    return redirect('home')
  else:
    return redirect('home')
 
@login_required 
def like_post(request, id):
    if request.method == 'GET':  
        username = request.user.username
        post = get_object_or_404(Post, id=id)
        like_filter = LikePost.objects.filter(post_id=id, username=username).first()
        
        if like_filter is None:
            new_like = LikePost.objects.create(post_id=id, username=username)
            post.no_of_likes += 1   
        else:
            # Remove the like
            like_filter.delete()
            post.no_of_likes -= 1
        post.save()
        return redirect('/#'+id)
        
      

@login_required   
def detail_post(request,id):
  post = Post.objects.get(id=id)
  profile = Profile.objects.get(user=request.user)
  return render(request,'LinkUp/home.html',{'posts':post,'profile':profile})

@login_required
def explore(request):
  post = Post.objects.all().order_by('-created_at')
  # profile = Profile.objects.get(user=request.user)
  return render(request,'LinkUp/explore.html',{'posts':post})

@login_required
def profile(request,id_user):
  user_object = User.objects.get(username=id_user)
  profile = Profile.objects.get(user=request.user)
  user_profile = Profile.objects.get(user=user_object)
  user_posts = Post.objects.filter(user=id_user).order_by('-created_at')
  user_post_length = len(user_posts)
  follower = request.user.username
  user = id_user
  if Follower.objects.filter(follower=follower,user=user).first():
    follow_unfollow = 'Unfollow'
  else:
    follow_unfollow = 'Follow'
  user_followers =len(Follower.objects.filter(user=id_user))
  user_following = len(Follower.objects.filter(follower=id_user))
  context = {
    'user_object':user_object,
    'profile':profile,
    'user_profile':user_profile,
    'user_posts':user_posts,
    'user_posts_length':user_post_length,
    'follow_unfollow':follow_unfollow,
    'user_followers':user_followers,
    'user_following':user_following
    

  }
  
  if request.user.username == id_user:
    if request.method == 'POST':
      if request.FILES.get('image') == None:
        image = user_profile.profile_img
        bio = request.POST.get('bio')
        location = request.POST.get('location')
        
        user_profile.profile_img = image
        user_profile.bio = bio 
        user_profile.location = location
        user_profile.save()
      if request.FILES.get('image') !=None:
        image = request.FILES.get('image')
        bio = request.POST.get('bio')
        location = request.POST.get('location')
        
        user_profile.profile_img = image
        user_profile.bio = bio 
        user_profile.location = location
        user_profile.save()
      return redirect('/profile/'+id_user)
    else:
      return render(request,'LinkUp/profile.html',context)
        
  return render(request,'LinkUp/profile.html',context)
 
@login_required 
def follow(request):
  if request.method == 'POST':
    follower = request.POST.get('follower')
    user = request.POST.get('user')
    
    if Follower.objects.filter(follower=follower,user=user).first():
      delete_follower = Follower.objects.get(follower=follower,user=user)
      delete_follower.delete()
      return redirect('/profile/'+user)
    else:
      new_follower = Follower.objects.create(follower=follower,user=user)
      new_follower.save()
      return redirect('/profile/'+user)
  else:
    return redirect('home')
 
@login_required 
def delete_post(request,id):
  post = Post.objects.get(id=id)
  post.delete()
  return redirect('/profile/'+request.user.username)

@login_required
def search_result(request):
  query = request.GET.get('q')
  users = Profile.objects.filter(user__username__icontains=query)
  posts = Post.objects.filter(caption__icontains=query)
  context ={
    'query':query,
    'users':users,
    'posts':posts
  }
  return render(request,'LinkUp/search_users.html',context)
  
  
      