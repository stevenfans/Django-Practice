from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'process_loc', views.process_loc, name='process_loc'),
    url(r'goToResults', views.goToResults, name='goToResults'),
    url(r'reload',views.reload, name='reload'),
    url(r'asdf',views.asdf, name='asdf')
]