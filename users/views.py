from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def logoutViews(request):
    logout(request)
    return HttpResponseRedirect(reverse('blogs:posts'))

def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data = request.POST)

        if form.is_valid():
            novoUsuario = form.save()
            authenticated_user = authenticate(username = novoUsuario.username,
                                              password = request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('blogs:posts'))

    context = {'form': form}
    return render(request, 'users/register.html', context)