from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from .models import Department, Designation, Faculty, Education, Course, Student, Journal, Conference, ResearchInterest, ProfessionalExperience, Achievement, AdministrativeResponsibility
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
            faculty = Faculty.objects.create()
            faculty.user = request.user
            faculty.save()
            # return redirect('info')
            return redirect(reverse('info', args=(faculty.id,)))
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

class FacultyCreate(CreateView):
	model=Faculty
	fields = '__all__'


class StudentCreate(CreateView):
	model = Student
	fields = '__all__'
	template_name = 'homepage/faculty_form.html'

	def get(self, request, *args, **kwargs):
	    self.object = None
	    pk = kwargs.get('pk')
	    faculty = get_object_or_404(Faculty, pk=pk)
	    context_data = self.get_context_data()
	    context_data.update(faculty=faculty)
	    return self.render_to_response(context_data)

class CourseCreate(CreateView):
	model = Course
	fields = '__all__'
	template_name = 'homepage/faculty_form.html'

class FacultyUpdate(UpdateView):
	model=Faculty
	fields = '__all__'
	template_name = 'homepage/faculty_form.html'
	# exclude = ['user']

def FacultyProfile(request):
	faculty = request.user.faculty
	return render(request, 'homepage/faculty_detail.html', context={'faculty': faculty})

def FacultyAttributes(request, fac_id, attr_id):
	faculty = Faculty.objects.get(id=int(fac_id))
	if attr_id == "0":		
		return render(request, 'homepage/faculty_about.html', context={'faculty': faculty})	
	if attr_id == "1":
		return render(request, 'homepage/faculty_publications.html', context={'faculty': faculty})
	if attr_id == "2":
		return render(request, 'homepage/faculty_teaching.html', context={'faculty': faculty})

from .forms import FacultyForm

def FacultyRegister(request):
	if request.method == 'POST' or hasattr(request.user, 'faculty'):
		faculty = Faculty.objects.create()

		form = FacultyForm(request.POST)
		if form.is_valid():
			faculty.first_name = form.cleaned_data['first_name']
			faculty.last_name = form.cleaned_data['last_name']

			# faculty.profile_picture = form.cleaned_data['profile_picture']
			faculty.residential_phone = form.cleaned_data['residential_phone']
			faculty.office_phone = form.cleaned_data['office_phone']

			faculty.iitg_email = form.cleaned_data['iitg_email']
			faculty.other_email = form.cleaned_data['other_email']

			faculty.room_number = form.cleaned_data['room_number']
			faculty.designation = form.cleaned_data['designation']
			faculty.department = form.cleaned_data['department']

			# faculty.biography = form.cleaned_data['biography']
			faculty.user = request.user

			faculty.save()

			return redirect(reverse('faculty-detail', args=(faculty.id,)))
			# return redirect(reverse('index'))
		else:
			form=FacultyForm()
			return render(request, 'signup_details.html', {'form': form})

	else:
		form = FacultyForm()
		return render(request, 'signup_details.html', {'form': form})

from .forms import StudentForm

def AddStudent(request, pk):
	faculty = Faculty.objects.get(id=int(pk))
	if request.method == 'POST':
		student = Student.objects.create()
		form = StudentForm(request.POST)
		if form.is_valid():
			student.first_name = form.cleaned_data['first_name']
			student.last_name = form.cleaned_data['last_name']
			student.topic = form.cleaned_data['topic']
			student.start_year = form.cleaned_data['start_year']
			student.end_year = form.cleaned_data['end_year']
			student.degree = form.cleaned_data['degree']

			student.faculty = faculty
			student.save()
			return redirect(reverse('faculty-detail', args=(faculty.id,)), context={'faculty': faculty})
	else:
		form = StudentForm()
		return render(request, 'homepage/faculty_form.html', context={'form': form, 'faculty': faculty})