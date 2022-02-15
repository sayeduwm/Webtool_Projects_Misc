from django.conf.urls import url
from django.contrib import admin
from main import views
from django.urls import path

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^$', views.login, name='login'),
  url(r'^reg/$', views.register, name='register'),
  url(r'^logout/$', views.logout, name='logout'),
  url(r'^admin_page/$', views.admin_page, name='admin_page'),
  path('$', views.Home.as_view(),name='user_logged'),
]
