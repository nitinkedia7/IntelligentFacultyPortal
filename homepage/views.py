from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import render, redirect
from .models import Department, Designation, Faculty, Education, Course, Journal, Conference, ResearchInterest, ProfessionalExperience, Achievement, AdministrativeResponsibility
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.core.urlresolvers import reverse

def index(request):
	dep = Department.objects.all
	return render(request, 'index.html',context={'dep': dep})

class DepartmentDetail(generic.DetailView):
	model = Department

class FacultyDetail(generic.DetailView):
	model = Faculty

def SignUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

class FacultyCreate(CreateView):
	model=Faculty
	fields = '__all__'

def FacultyProfile(request):
	faculty = request.user.faculty
	return render(request, 'homepage/faculty_detail.html', context={'faculty': faculty})

# BookInstance.objects.filter(status__exact='o').order_by('due_back')  
def FacultyAbout(request, pk):
	faculty = Faculty.objects.filter(id=pk)
	return render(request, 'homepage/faculty_about.html', context={'faculty': faculty})

def FacultyTeaching(request, pk):
	faculty = Faculty.objects.filter(id=pk)
	return render(request, 'homepage/faculty_teaching.html', context={'faculty': faculty})

def FacultyPublications(request, pk):
	faculty = Faculty.objects.filter(id=pk)
	return render(request, 'homepage/faculty_publications.html', context={'faculty': faculty})

def FacultyAttributes(request, fac_id, attr_id):
	if True:
		faculty = Faculty.objects.get(id=fac_id)
		return render(request, 'homepage/faculty_about.html', context={'faculty': faculty})
	if attr_id == 1:
		faculty = Faculty.objects.get(id=fac_id)
		return render(request, 'homepage/faculty_teaching.html', context={'faculty': faculty})
	if attr_id == 2:
		faculty = Faculty.objects.get(id=fac_id)
		return render(request, 'homepage/faculty_publications.html', context={'faculty': faculty})
	# faculty = Faculty.objects.get(id=fac_id)
	# return render(request, 'homepage/faculty_publications.html', context={'faculty': faculty})