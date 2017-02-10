from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.posts, name='posts'),
    url(r'^novoPost/$', views.novoPost, name='novoPost'),
    url(r'^editPost/(?P<post_id>\d+)/$', views.editPost, name='editPost'),
	url(r'^detailPost/(?P<post_id>\d+)/$', views.detailPost, name='detailPost'),
]
