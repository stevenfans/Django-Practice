from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'spin'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'process_loc', views.process_loc, name='process_loc'),
    url(r'goToResults', views.goToResults, name='goToResults')
]