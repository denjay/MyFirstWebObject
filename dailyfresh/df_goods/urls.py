from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(\d+)/$', views.detail),
    url(r'^list_(\d+)_(\d+)/$', views.goods_list),
]

