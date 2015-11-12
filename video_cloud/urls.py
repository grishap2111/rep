from django.conf.urls import patterns, include, url
from django.contrib import admin

from video_cloud import views

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^index/$', views.index, name='index'),
                       url(r'^cameras/$', views.cameras, name='cameras'),
                       url(r'^pricing/$', views.pricing, name='pricing'),
                       url(r'^contact/$', views.contact, name='contact'),
                       url(r'^accounts/', include('accounts.urls', namespace="accounts")),
                       )
