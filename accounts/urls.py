from django.conf.urls import patterns, include, url

from accounts import views

urlpatterns = patterns('',  # url(r'^', views.login_in, name='login'),
                       url(r'^', views.login, name='login'),
                       url(r'^login/', views.login, name='login'),
                       url(r'^logout/', views.logout, name='logout'),
                       url(r'^register/', views.register, name='register'),
                       )
