from django.shortcuts import render, HttpResponse, redirect
import datetime 
from .models import Post, Profile, City
class Data:
  def __init__(self, test):
    self.test = test

# class Post:
#     def __init__(self):
#         self.title = "Test"
#         self.body = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus, vero, obcaecati, aut, error quam sapiente nemo saepe quibusdam sit excepturi nam quia corporis eligendi eos magni recusandae laborum minus inventore?"
#         self.img = "http://placehold.it/900x300" 
#         self.author = "Jimmy"
#         self.date_created = datetime.datetime.now()

data = {
    Data("TESTING DATA")
}
# Create your views here.

def home(request):
    context = {
        'data': data
    }
    return render(request, 'home.html', context)

def profile(request):
    profile = Profile.objects.get(id=request.user.id)
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

def edit_profile(request, profile_id):
    profile = Profile.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save()
            return redirect('detail', profile.id)
    else:
        form = ProfileForm(instance=profile)
        return render(request, 'profileEdit.html', {'form': form})