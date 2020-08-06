from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('profile/', views.profile, name='profile'),
  path('profile/<int:profile_id>/edit/', views.edit_profile, name='edit_profile'),
  path('post/<int:post_id>', views.post, name='post'),
]