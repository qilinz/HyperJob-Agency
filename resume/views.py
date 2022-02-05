from django.shortcuts import render
from django.views import View
from .models import Resume


# Create your views here.
class ResumeView(View):
    def get(self, request, *args, **kwargs):
        resumes = Resume.objects.all()
        return render(request, 'resume.html', context={'resumes': resumes})
