from django.shortcuts import render
from .models import Department, Designation, Faculty, Education, Course, Journal, Conference, ResearchInterest, ProfessionalExperience, Achievement, AdministrativeResponsibilitie
# Create your views here.

def index(request):
    return render(
        request,
        'index.html',
    )