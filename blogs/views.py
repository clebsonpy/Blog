from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import PostForm

# Create your views here.
def posts(request):
    posts = BlogPost.objects.order_by('-dataAdd')
    context = {'posts': posts}
    return render(request, 'blogs/posts.html', context)

@login_required
def novoPost(request):
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            novoPost = form.save(commit=False)
            novoPost.usuario = request.user
            novoPost.save()
            return HttpResponseRedirect(reverse('blogs:posts'))

    context = {'form':form}
    return render(request, 'blogs/novoPost.html', context)

@login_required
def editPost(request, post_id):
    post = BlogPost.objects.get(id = post_id)
    if post.usuario != request.user:
        raise Http404

    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:posts'))

    context = {'post': post, 'form': form}
    return render(request, 'blogs/editPost.html', context)