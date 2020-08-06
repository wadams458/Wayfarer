from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('profile/', views.profile, name='profile'),
  path('post/<int:post_id>', views.post, name='post'),
  path('accounts/signup', views.signup, name='signup'),
]