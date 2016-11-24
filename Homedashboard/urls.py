"""HouseManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from Homedashboard.views import login_view, logout_view
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name="index"),
    url(r'^tenant/$', views.tenant, name="tenant"),
    url(r'^createuser/$', views.createuser,name="createuser"),
    url(r'^newtenant/$', views.newtenant,name="newtenant"),
    url(r'^roomreg/$', views.roomregistration,name="roomreg"),
    url(r'^rooms/$', views.rooms,name="rooms"),
    url(r'^$', login_view,name="login"),
    url(r'^logout/$', logout_view, name="logout"),

]
