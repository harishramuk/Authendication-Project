"""authendication33 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from TestApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepageview),
    path('java/',views.javaexamview),
    path('python/',views.pythonexamview),
    path('aptitude/',views.aptitudeexamview),
    path('accounts/',include('django.contrib.auth.urls')),
    path('logout/',views.logoutview),
    path('signup/',views.signupview)
    ]
