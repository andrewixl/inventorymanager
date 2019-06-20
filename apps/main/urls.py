from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^profile$', views.profile),
    url(r'^inventory/(?P<id>\w+)/$', views.inventory),
    url(r'^checkedout/(?P<id>\w+)/$', views.checkedout),
]