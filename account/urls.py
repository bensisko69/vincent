from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^account', views.account, name='account'),
    url(r'^validatingForm', views.validatingForm, name='validatingForm'),
]