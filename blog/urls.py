# blog/urls.py
from django.urls import path
from users import views as user_views  
from blog import views as blog_views 
urlpatterns = [
    path('', blog_views.home, name='blog-home'),  
    path('about/', blog_views.about, name='blog-about'), 
    path('profile/', blog_views.profile, name='blog-profile'),  
    path('register/', user_views.register, name='blog-register'),  
    path('login/', user_views.login, name='blog-login'), 
]
