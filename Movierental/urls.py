"""Movierental URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from . import views
from Movierental.views import MovieList, CustomerList, CustList, MoList
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path("index",views.index, name="index"),
    path("logoutuser",views.logout_view, name="logout"),
    path("homepage",views.homepage, name="homepage"),

    path("addcust",views.addcust,name="addcust"),

    path("addmovies",views.addmovies,name="addmovies"),
    path("availablemovies",views.availablemovies,name="availablemovies"),
    # path("listofcustomers",views.listofcustomers,name="listofcustomers"),
    path("listofmovies",views.listofmovies,name="listofmovies"),
    path("searchcustomers",views.searchcust,name="searchcust"),
    path("searchmovies",views.searchmovies,name="searchmovies"),
    path("assignmovies",views.assignmovies,name="assignmovies"),
    path("logout_view",views.logout_view, name="logout_view"),
    path("listofcustomers/delete/<int:id>",views.delcust,name="delcust"),
    path("listofmovies/delete/<int:id>",views.delmovie,name="delmovie"),
    path("listofcustomers/update/<int:id>/",views.updatecust,name="updatecust"),
    path("listofcustomers",views.searchcust,name="searchcust"),
    path("mjson/",MovieList.as_view(),name="mjson"),
    path("cjson/",CustomerList.as_view(),name="cjson"),
    path("cjson/<int:id>",CustList.as_view(),name="CustList"), #
    path("mjson/<int:id>",MoList.as_view(),name="MoList"),

]

urlpatterns = format_suffix_patterns(urlpatterns)