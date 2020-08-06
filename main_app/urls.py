from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('profile/', views.profile, name='profile'),
  path('profile/edit', views.edit_profile, name='profile_edit'),
  path('post/<int:post_id>', views.post, name='post'),
  path('login', views.custom_login, name='custom_login'),
  path('signup', views.signup, name='signup'),
  path('cities', views.cities, name='cities'),
]