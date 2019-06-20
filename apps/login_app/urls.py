from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^signin$', views.signin),
    url(r'^signup$', views.signup),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),

]
