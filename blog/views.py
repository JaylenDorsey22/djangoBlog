from django.shortcuts import render, HttpResponse



posts= [
    {
    'author': 'Jaylen22',
    'title': 'Blog Post 1',
    'content':'First post content',
    'date_posted': 'December 11, 2024'
    },
    {
    'author': 'AlyssaCarter5',
    'title': 'Blog Post 2',
    'content':'Second post content',
    'date_posted': 'December 1 , 2024'
    }

]
# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html',context, )


    

def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})

def profile(request):
    return render(request, 'blog/profile.html')