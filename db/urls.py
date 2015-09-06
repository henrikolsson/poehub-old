from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^skillgem/?$', views.skillgems, name='skillgems'),
    url(r'^skillgem/([0-9]+)$', views.skillgem, name='skillgem'),
]
