from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import BlogPost
from .forms import PostForm

# Create your views here.
def posts(request):
    posts = BlogPost.objects.order_by('-dataAdd')
    context = {'posts': posts}
    return render(request, 'blogs/posts.html', context)

def novoPost(request):
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:posts'))

    context = {'form':form}
    return render(request, 'blogs/novoPost.html', context)