from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name="index"),
    #12.0.0.1/polls/1
]
