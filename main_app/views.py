from django.shortcuts import render, HttpResponse, redirect
from .models import Post, Profile, City
from .forms import ProfileForm, UserForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def home(request):
    posts = Post.objects.all().order_by('-created_at')[:3]
    context = {
        'posts': posts
    }
    # return HttpResponse(f"{posts[0]} {posts[1]}")
    return render(request, 'home.html', context)


# ------------------- CITIES/POSTS -------------------

def cities(request, city_id):
    cities = City.objects.all()
    posts = Post.objects.filter(city=city_id).order_by('-created_at')
    context = {
        'cities': cities,
        'posts': posts
    }
    return render(request, 'cities.html', context)

def post(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post
    }
    return render(request, 'post.html', context)


# ------------------- PROFILE -------------------

def profile(request):
    profile = Profile.objects.get(user=request.user.id)
    posts = Post.objects.filter(user=request.user.id)
    context = {
        'profile': profile,
        'posts': posts
    }
    return render(request, 'profile.html', context)

def edit_profile(request):
    profile = Profile.objects.get(user=request.user.id)
    user = request.user
    if request.method == 'POST':
      profile_form = ProfileForm(request.POST, instance=profile)
      user_form = UserForm(request.POST, instance=user)

      if profile_form.is_valid() and user_form.is_valid():
        profile = profile_form.save()
        user = user_form.save()
        return redirect('profile')
    else:
      # Create Form
      profile_form = ProfileForm(instance=profile)
      user_form = UserForm(instance=user)
      # Render Form
      return render(request, 'profileEdit.html', {'profile_form': profile_form, 'user_form': user_form})


# ------------------- LOGIN/AUTH RELATED -------------------

def custom_login(request):
    error_message = ''
    signup_form = UserCreationForm()
    login_form = AuthenticationForm()
    context = {'signup_form': signup_form, 'login_form': login_form, 'error_message': error_message}
    return render(request, 'registration/login.html', context)

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
    signup_form = UserCreationForm()
    login_form = AuthenticationForm()
    context = {'signup_form': signup_form, 'login_form': login_form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def cities(request):
    return render(request, 'cities.html')

