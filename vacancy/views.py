from django.shortcuts import render
from django.views import View
from .models import Vacancy


# Create your views here.
class VacancyView(View):
    def get(self, request, *args, **kwargs):
        vacancies = Vacancy.objects.all()
        return render(request, 'vacancy.html', context={"vacancies": vacancies})