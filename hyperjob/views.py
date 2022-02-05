from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.shortcuts import redirect
from django import forms
from django.http import HttpResponse

from resume.models import Resume
from vacancy.models import Vacancy


# Create your views here.
class MenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'menu.html')


class MySignUpView(CreateView):
    form_class = UserCreationForm
    success_url = '/login'
    template_name = 'signup.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'


class ProfileForm(forms.Form):
    description = forms.CharField(label='Description', max_length=1024)


class MyProfileView(View):
    def get(self, request, *args, **kwargs):
        current_user = request.user
        is_authenticated = current_user.is_authenticated
        is_staff = current_user.is_staff

        if is_authenticated:
            if is_staff:
                return redirect("/vacancy/new")
            return redirect("/resume/new")

        return render(request, "home.html")


class MyResumeView(View):
    def get(self, request, *args, **kwargs):
        form = ProfileForm()
        return render(request, "new_resume.html", context={"form": form})

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST)
        current_user = request.user
        is_authenticated = current_user.is_authenticated
        is_staff = current_user.is_staff
        if is_authenticated and (not is_staff) and form.is_valid():
            data = form.cleaned_data
            description = data.get("description")
            Resume.objects.create(description=description, author=current_user)
            return redirect('/home')

        return HttpResponse(status=403)


class MyVacancyView(View):
    def get(self, request, *args, **kwargs):
        form = ProfileForm()
        return render(request, "new_vacancy.html", context={"form": form})

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST)
        current_user = request.user
        is_authenticated = current_user.is_authenticated
        is_staff = current_user.is_staff
        if is_authenticated and is_staff and form.is_valid():
            data = form.cleaned_data
            description = data.get("description")
            Vacancy.objects.create(description=description, author=current_user)
            return redirect('/home')

        return HttpResponse(status=403)