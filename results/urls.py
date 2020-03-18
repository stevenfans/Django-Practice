from django.conf.urls import url
from . import views
from django.urls import path
from roulette import views
from results import views

app_name = 'result'

urlpatterns = [
    url(r'^$',views.foodView.as_view()),
    url(r'^test/',views.test,name='test'),

]