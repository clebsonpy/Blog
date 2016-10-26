from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.posts, name='posts'),
    url(r'^novoPost/$', views.novoPost, name='novoPost'),
]