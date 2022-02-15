from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from main import views

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  path(r'', views.Home.as_view()),
    path(r'person', views.Person.as_view()),
    path(r'friend', views.friend.as_view()),

]
