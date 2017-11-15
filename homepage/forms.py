from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Department, Designation, Faculty, Education, Course, Journal, Conference, ResearchInterest, ProfessionalExperience, Achievement, AdministrativeResponsibilitie

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2', )