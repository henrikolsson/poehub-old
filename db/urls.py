from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^skillgem/?$', views.skillgems, name='skillgems'),
    url(r'^skillgem/([^/]+)$', views.skillgem, name='skillgem'),
    url(r'^itemclass/?$', views.itemclasses, name='itemclasses'),
    url(r'^itemclass/([^/]+)$', views.itemclass, name='itemclass'),
    url(r'^mod/?$', views.mod, name='mod'),
    url(r'^mod/([^/]+)?$', views.mods, name='mods'),
    url(r'^quest/?$', views.quests, name='quests'),
    url(r'^quest/([^/]+)$', views.quest, name='quest'),
]
