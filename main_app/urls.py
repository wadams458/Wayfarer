from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),

  path('profile/<int:user_id>', views.profile, name='profile'),
  path('profile/<int:user_id>/edit', views.edit_profile, name='profile_edit'),
  
  path('cities/<int:city_id>', views.cities, name='cities'),

  path('post/<int:post_id>', views.post, name='post'),
  path('post/<int:post_id>/edit', views.post_edit, name='post_edit'),
  path('post/<int:post_id>/delete', views.post_delete, name='post_delete'),
  path('post/add', views.post_add, name='post_add'),
  
  path('login', views.custom_login, name='custom_login'),
  path('my-profile', views.my_profile, name='my_profile'),
  path('signup', views.signup, name='signup'),

  path('about',views.about, name='about'),
]