from django.conf.urls import patterns, include, url
from blog import views

urlpatterns = patterns('',
    # ex: /blog/
    # url(r'^$', views.index),
    # ex: /blog/list/
    url(r'^list/$', views.list),
    # ex: /blog/entry/5/
    url(r'^entry/(?P<entry_id>\d+)/$', views.detail),
)
