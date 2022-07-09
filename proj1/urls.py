"""proj1 URL Configuration

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
from django.urls import path
from . import cool

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",cool.index,name="index"),
    path("home",cool.home,name="home"),
    path("about",cool.about,name="about"),
    # path("spaceremover",cool.spaceremover,name="spaceremover"),
    path("removepunctuations",cool.removepunctuations,name="removepunctuations")
    # path("capitalletters",cool.capitalletters,name="capitalletters")


]
