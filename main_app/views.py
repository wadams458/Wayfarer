from django.shortcuts import render, HttpResponse, redirect
from .models import Post, Profile, City
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    return render(request, 'home.html')


def profile(request):
    profile = Profile.objects.get(user=request.user.id)
    posts = Post.objects.filter(user=request.user.id)
    context = {
        'profile': profile,
        'posts': posts
    }
    return render(request, 'profile.html', context)


def post(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post
    }
    return render(request, 'post.html', context)


def signup(request):
    error_message = ''
    if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
        # This will add the user to the database
        user = form.save()
        print(user.id)
        Profile.objects.create(user=user)
        # This is how we log a user in via code
        login(request, user)
        return redirect('profile')
      else:
        error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)