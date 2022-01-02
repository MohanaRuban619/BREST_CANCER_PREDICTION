"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from first_app import views
# from django.conf import settings
# from django.conf.urls.static import static
# from rest_framework import routers
# routers = routers.DefaultRouter()
from first_app import views
# from mysite.settings import STATIC_URL, STATICFILES_DIRS
from first_app.views import FormView


urlpatterns = [
    # path('static/',settings.STATIC_URL,include("static.urls")),
    path('form/',views.FormView,name='forms'),
    path("result/",views.status, name= "status"),
]
