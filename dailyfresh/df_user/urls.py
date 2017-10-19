from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^check_uname/$', views.check_uname),
    url(r'^submit/$', views.submit),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^login_handle/$', views.login_handle),
    url(r'^info/$', views.info),
    url(r'^order/$', views.order),
    url(r'^site/$', views.site),
]