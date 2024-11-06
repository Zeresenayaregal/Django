from django.shortcuts import render
from django.views.generic import ListView
from .models import Post



def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # The default format for the direction of the funtion is the following '<app>/<modelNmae>_<viewtype>.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
