from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^manyToMany$', views.manyToManyTable, name='manyToManyTable'),
    url(r'^calories/$', views.calories_view, name='calories'),
    url(r'^diary/$', views.diary_view, name='diary')
]
