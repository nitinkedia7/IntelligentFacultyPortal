from django.views import generic
from django.shortcuts import render
from .models import Department, Designation, Faculty, Education, Course, Journal, Conference, ResearchInterest, ProfessionalExperience, Achievement, AdministrativeResponsibilitie
# Create your views here.

def index(request):
	dep = Department.objects.all
	return render(request, 'index.html',context={'dep': dep})

class DepartmentDetail(generic.DetailView):
	model = Department

