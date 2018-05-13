from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from .models import Department, Designation, Faculty, Education, Course, Student, Journal, Conference, ProfessionalExperience, Achievement, AdministrativeResponsibility, Project
from django.contrib.auth import login, authenticate
from django.urls import reverse
from .forms import SignupForm, SearchForm
from django.contrib.auth.decorators import login_required

def index(request):
	form = SearchForm()
	dep = Department.objects.all
	return render(request, 'index.html',context={'dep': dep, 'form': form,})

def Search(request):
	if request.method == "POST":
		form = SearchForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['username']
			faculty = Faculty.objects.filter(first_name__contains=name)
			return render(request, 'homepage/faculty_search.html',context={'matching_faculty' : faculty,})
	else:
		return redirect(index)

class DepartmentDetail(generic.DetailView):
	model = Department

class FacultyDetail(generic.DetailView):
	model = Faculty

def SignUp(request, dept):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            faculty = Faculty.objects.create()
            faculty.user = request.user
            faculty.department = Department.objects.get(id=dept)
            faculty.save()
            return redirect(reverse('faculty-update-profile', args=(faculty.id,)))
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# class FacultyCreate(CreateView):
# 	model=Faculty
# 	fields = '__all__'


# class StudentCreate(CreateView):
# 	model = Student
# 	fields = '__all__'
# 	template_name = 'homepage/faculty_form.html'

# 	def get(self, request, *args, **kwargs):
# 	    self.object = None
# 	    pk = kwargs.get('pk')
# 	    faculty = get_object_or_404(Faculty, pk=pk)
# 	    context_data = self.get_context_data()
# 	    context_data.update(faculty=faculty)
# 	    return self.render_to_response(context_data)


# class FacultyUpdate(UpdateView):
# 	model=Faculty
# 	fields = '__all__'
# 	template_name = 'homepage/faculty_form.html'
# 	# exclude = ['user']

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


from .forms import FacultyForm, StudentForm, CourseForm, EducationForm, AchievementForm, ProfessionalExperienceForm, AdministrativeResponsibilityForm, ConferenceForm, JournalForm , ProjectForm

def UpdateFaculty(request, pk):
	faculty = Faculty.objects.get(id=pk)
	if request.method == 'POST':
		form = FacultyForm(request.POST)
		if form.is_valid():
			faculty.first_name = form.cleaned_data['first_name']
			faculty.last_name = form.cleaned_data['last_name']
			if request.FILES:
				faculty.profile_picture = request.FILES['profile_picture']			
			faculty.residential_phone = form.cleaned_data['residential_phone']
			faculty.office_phone = form.cleaned_data['office_phone']
			faculty.iitg_email = form.cleaned_data['iitg_email']
			faculty.other_email = form.cleaned_data['other_email']
			faculty.room_number = form.cleaned_data['room_number']
			faculty.designation = form.cleaned_data['designation']
			faculty.department = form.cleaned_data['department']
			faculty.biography = form.cleaned_data['biography']
			faculty.interests = form.cleaned_data['interests']
			faculty.save()
			return redirect(reverse('faculty-detail', args=(faculty.id,)))
	else:
		form = FacultyForm(instance=faculty)
	return render(request, 'homepage/faculty_form.html', context={'form': form, 'faculty': faculty})

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
			return redirect(reverse('faculty-detail', args=(faculty.id,)))
	else:
		form = StudentForm()
	return render(request, 'homepage/faculty_form.html', context={'form': form, 'faculty': faculty})

def AddCourse(request, pk):
	faculty = Faculty.objects.get(id=int(pk))
	if request.method == 'POST':
		course = Course.objects.create()
		form = CourseForm(request.POST)
		if form.is_valid():
			course.name = form.cleaned_data['name']
			course.code = form.cleaned_data['code']
			course.semester = form.cleaned_data['semester']
			course.year = form.cleaned_data['year']

			course.faculty = faculty
			course.save()
			return redirect(reverse('faculty-detail', args=(faculty.id,)))
	else:
		form = CourseForm()
	return render(request, 'homepage/faculty_form.html', context={'form': form, 'faculty': faculty})


def AddAchievement(request, pk):
	faculty = Faculty.objects.get(id=int(pk))
	if request.method == 'POST':
		achievement = Achievement.objects.create()
		form = AchievementForm(request.POST)
		if form.is_valid():
			achievement.award = form.cleaned_data['award']
			achievement.awarded_by = form.cleaned_data['awarded_by']
			achievement.year = form.cleaned_data['year']

			achievement.faculty = faculty
			achievement.save()
			return redirect(reverse('faculty-detail', args=(faculty.id,)))
	else:
		form = AchievementForm()
	return render(request, 'homepage/faculty_form.html', context={'form': form, 'faculty': faculty})

def AddEducation(request, pk):
	faculty = Faculty.objects.get(id=int(pk))
	if request.method == 'POST':
		education = Education.objects.create()
		form = EducationForm(request.POST)
		if form.is_valid():
			education.degree = form.cleaned_data['degree']
			education.branch = form.cleaned_data['branch']
			education.institute = form.cleaned_data['institute']
			education.duration = form.cleaned_data['duration']

			education.faculty = faculty
			education.save()
			return redirect(reverse('faculty-detail', args=(faculty.id,)))
	else:
		form = EducationForm()
	return render(request, 'homepage/faculty_form.html', context={'form': form, 'faculty': faculty})

def AddJournal(request, pk):
	faculty = Faculty.objects.get(id=int(pk))
	if request.method == 'POST':
		journal = Journal.objects.create()
		form = JournalForm(request.POST)
		if form.is_valid():
			journal.title = form.cleaned_data['title']
			journal.contributors = form.cleaned_data['contributors']
			journal.book = form.cleaned_data['book']
			journal.year = form.cleaned_data['year']
			journal.faculty = faculty
			journal.save()
			return redirect(reverse('faculty-detail', args=(faculty.id,)))
	else:
		form = JournalForm()
	return render(request, 'homepage/faculty_form.html', context={'form': form, 'faculty': faculty})

def AddConference(request, pk):
	faculty = Faculty.objects.get(id=int(pk))
	if request.method == 'POST':
		conference = Conference.objects.create()
		form = ConferenceForm(request.POST)
		if form.is_valid():
			conference.participants = form.cleaned_data['participants']
			conference.topic = form.cleaned_data['topic']
			conference.event = form.cleaned_data['event']
			conference.year = form.cleaned_data['year']
			conference.faculty = faculty
			conference.save()
			return redirect(reverse('faculty-detail', args=(faculty.id,)))
	else:
		form = ConferenceForm()
	return render(request, 'homepage/faculty_form.html', context={'form': form, 'faculty': faculty})

def AddProfessionalExperience(request, pk):
	faculty = Faculty.objects.get(id=int(pk))
	if request.method == 'POST':
		proex = ProfessionalExperience.objects.create()
		form = ProfessionalExperienceForm(request.POST)
		if form.is_valid():
			proex.designation = form.cleaned_data['designation']
			proex.institute = form.cleaned_data['institute']
			proex.duration = form.cleaned_data['duration']
			proex.faculty = faculty
			proex.save()
			return redirect(reverse('faculty-detail', args=(faculty.id,)))
	else:
		form = ProfessionalExperienceForm()
	return render(request, 'homepage/faculty_form.html', context={'form': form, 'faculty': faculty})

def AddAdministrativeResponsibility(request, pk):
	faculty = Faculty.objects.get(id=int(pk))
	if request.method == 'POST':
		ar = AdministrativeResponsibility.objects.create()
		form = AdministrativeResponsibilityForm(request.POST)
		if form.is_valid():
			ar.designation = form.cleaned_data['designation']
			ar.start = form.cleaned_data['start']
			ar.end = form.cleaned_data['end']
	
			ar.faculty = faculty
			ar.save()
			return redirect(reverse('faculty-detail', args=(faculty.id,)))
	else:
		form = AdministrativeResponsibilityForm()
	return render(request, 'homepage/faculty_form.html', context={'form': form, 'faculty': faculty})

def AddProject(request, pk):
	faculty = Faculty.objects.get(id=pk)
	if request.method == 'POST':
		project = Project.objects.create()
		form = ProjectForm(request.POST)
		if form.is_valid():
			project.title = form.cleaned_data['title']
			project.sponsor = form.cleaned_data['sponsor']
			project.budget = form.cleaned_data['budget']
			project.duration = form.cleaned_data['duration']
			project.role = form.cleaned_data['role']
			ar.faculty = faculty
			ar.save()
			return redirect(reverse('faculty-detail', args=(faculty.id,)))
	else:
		form = ProjectForm()
	return render(request, 'homepage/faculty_form.html', context={'form': form, 'faculty': faculty})	

from .mail_scan import mailscan
@login_required
def AutoUpdate(request, pk):
	info = mailscan()
	print(info)
	if info['type'] == "journal":
		journal = Journal.objects.create()
		journal.title = info['title']
		journal.book = info['paper']
		journal.contributors = info['contrib']
		journal.faculty = Faculty.objects.get(id=pk)
		journal.save()
	elif info['type'] == "promotion":
		faculty = Faculty.objects.get(id=pk)
		print(faculty.designation.designation)
		faculty.designation.designation = info['designation']
		print(faculty.designation.designation)
	elif info['type'] == "adminres":	
		admres = AdministrativeResponsibility.objects.create()
		admres.designation = info['responsibility']
		admres.start = info['from']
		admres.faculty = Faculty.objects.get(id=pk)
		admres.save()
	elif info['type'] == "project":	
		project = Project.objects.create()
		project.sponsor = info['sponsor']
		project.title = info['title']
		project.budget = info['budget']
		project.role = info['role']
		project.faculty = Faculty.objects.get(id=pk)
		project.save()	
	return redirect(reverse('faculty-detail', args=(pk,)))