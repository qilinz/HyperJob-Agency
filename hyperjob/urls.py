"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views
from resume.views import ResumeView
from vacancy.views import VacancyView
from django.views.generic import RedirectView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('resumes/', ResumeView.as_view()),
    path('vacancies/', VacancyView.as_view()),
    path('login', views.MyLoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('signup', views.MySignUpView.as_view()),
    path('home', views.MyProfileView.as_view()),
    path('vacancy/new', views.MyVacancyView.as_view()),
    path('resume/new', views.MyResumeView.as_view()),
    path('login/', RedirectView.as_view(url='/login')),
    path('logout/', RedirectView.as_view(url='/logout')),
    path('signup/', RedirectView.as_view(url='/signup')),
    path('admin', admin.site.urls),
    path('', views.MenuView.as_view())
]
