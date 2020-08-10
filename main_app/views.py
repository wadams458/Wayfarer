from django.shortcuts import render, HttpResponse, redirect
from .models import Post, Profile, City
from .forms import ProfileForm, UserForm, PostForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def home(request):
    posts = Post.objects.all().order_by('-created_at')[:3]
    context = {
        'posts': posts
    }
    # return HttpResponse(f"{posts[0]} {posts[1]}")
    return render(request, 'home.html', context)

def about(request):
    
    # return HttpResponse(f"{posts[0]} {posts[1]}")
    return render(request, 'about.html')

# ------------------- CITIES -------------------

def cities(request, city_id):
    cities = City.objects.all()
    posts = Post.objects.filter(city=city_id).order_by('-created_at')
    selected_city = City.objects.get(id=city_id)
    context = {
        'cities': cities,
        'posts': posts,
        'selected_city': selected_city,
    }
    return render(request, 'cities.html', context)


# ------------------- POSTS -------------------

def post(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post
    }
    return render(request, 'posts/post.html', context)

@login_required
def post_add(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        new_post = form.save(commit=False)
        new_post.user = request.user
        new_post.save()

        return redirect('post', new_post.id)
    else:
      form = PostForm()
      return render(request, 'posts/post_add.html', {'form': form})

@login_required
def post_edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
      form = PostForm(request.POST, request.FILES, instance=post)
      if form.is_valid():
        post = form.save()
        return redirect('post', post.id)
    else:
      form = PostForm(instance=post)
    return render(request, 'posts/post_edit.html', {'form': form, 'post': post})

@login_required
def post_delete(request, post_id):
  post = Post.objects.get(id=post_id)
  city_id = post.city.id
  post.delete()
  return redirect('cities', city_id)

# ------------------- PROFILE -------------------

@login_required
def my_profile(request):
    return redirect('profile', request.user.id)

@login_required
def profile(request, user_id):
    profile = Profile.objects.get(user=user_id)
    posts = Post.objects.filter(user=profile.user.id)
    context = {
        'profile': profile,
        'posts': posts
    }
    return render(request, 'profile.html', context)

@login_required
def edit_profile(request, user_id):
    profile = Profile.objects.get(user=user_id)
    user = request.user
    if request.method == 'POST':
      profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
      user_form = UserForm(request.POST, instance=user)

      if profile_form.is_valid() and user_form.is_valid():
        profile = profile_form.save()
        user = user_form.save()
        return redirect('profile', user.id)
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
        return redirect('profile', user.id)
      else:
        error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    signup_form = UserCreationForm()
    login_form = AuthenticationForm()
    context = {'signup_form': signup_form, 'login_form': login_form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

