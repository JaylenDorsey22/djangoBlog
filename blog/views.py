from django.shortcuts import render, HttpResponse
from .models import Post
from users import views

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html',context, )


    

def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})

def profile(request):
    return render(request, 'blog/profile.html')

