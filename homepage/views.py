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
	dep = Department.objects.all()
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

# class FacultyDetail(generic.DetailView):
# 	model = Faculty

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

import httplib2
import pprint
import base64
from bs4 import BeautifulSoup
import re
from apiclient import errors
from .mail_scan import mailscan

from googleapiclient.discovery import build
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import CredentialsModel
from faculty_portal import settings
from oauth2client.contrib import xsrfutil
from oauth2client.client import flow_from_clientsecrets
from oauth2client.contrib.django_util.storage import DjangoORMStorage

# CLIENT_SECRETS, name of a file containing the OAuth 2.0 information for this
# application, including client_id and client_secret, which are found
# on the API Access tab on the Google APIs
# Console <http://code.google.com/apis/console>

FLOW = flow_from_clientsecrets(
    settings.GOOGLE_OAUTH2_CLIENT_SECRETS_JSON,
    scope='https://www.googleapis.com/auth/gmail.modify https://www.googleapis.com/auth/gmail.labels',
    redirect_uri='http://127.0.0.1:8000/home/oauth2callback')

def FacultyProfile(request, pk):
	faculty = Faculty.objects.get(id=pk)		
	if not (request.user.is_authenticated and int(pk) == request.user.faculty.id):
		return render(request, 'homepage/faculty_detail.html', context={'faculty': faculty})
	
	storage = DjangoORMStorage(CredentialsModel, 'id', request.user, 'credential')
	credential = storage.get()

	if credential is None or credential.invalid == True:
		FLOW.params['state'] = xsrfutil.generate_token(settings.SECRET_KEY,
														request.user)
		authorize_url = FLOW.step1_get_authorize_url()
		return HttpResponseRedirect(authorize_url)
	else:
		http = httplib2.Http()
		http = credential.authorize(http)
		service = build("gmail", "v1", http=http)
		# Call the Gmail API to get (relevant) messages
		results = service.users().messages().list(userId='me', q="-label:IFP  from:*.iitg.ernet.in subject:{designation responsibility Project paper}").execute()
		messages = results.get('messages', [])
		if not messages:
			print('No messages found.')
		else:
			# print(messages)
			print(len(messages))
			response = service.users().labels().list(userId='me').execute()
			labels = response['labels']
			for label in labels:
				if label['name'] == "IFP": labelId = label['id'] 
			for message in messages:
				msg = service.users().messages().get(userId='me', id=message['id']).execute()
				msg_labels = {'removeLabelIds': [], 'addLabelIds': [labelId]}
				msg1 = service.users().messages().modify(userId='me', id=message['id'], body=msg_labels).execute()
 				# pprint.pprint(msg)
				msg_dict = {'subject' : "", 'body' : ""}
				payload = msg['payload']
				# getting the Subject
				headr = payload['headers']
				for one in headr: 
					if one['name'] == 'Subject':
						msg_subject = one['value']
						msg_dict['subject'] = msg_subject
				# getting the message body
				if (payload['mimeType'] == 'text/plain'):
					msg_data = payload["body"]["data"]
					msg_body = base64.b64decode(msg_data.encode("ASCII")).decode("UTF-8")
					msg_dict['body'] = msg_body
				elif (payload['mimeType'] == "multipart/alternative"):
					for part in payload['parts']:
						if (part['mimeType'] == 'text/plain'):
							part_data = part['body']['data']
							part_body = base64.b64decode(part_data.encode("ASCII")).decode("UTF-8")
							msg_dict['body'] += part_body
				# pprint.pprint(msg_dict)
				info = mailscan(msg_dict)
				# pprint.pprint(info)
				pk = request.user.faculty.id
				if info['type'] == "journal":
					journal = Journal.objects.create()
					journal.title = info['title']
					journal.book = info['paper']
					journal.contributors = info['contrib']
					journal.faculty = Faculty.objects.get(id=pk)
					journal.save()
				elif info['type'] == "promotion":
					faculty = Faculty.objects.get(id=pk)
					faculty.designation.designation = info['designation']
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
		return render(request, 'homepage/faculty_detail.html', context={'faculty': faculty})

@login_required
def auth_return(request):
	print(request.GET)
	if not xsrfutil.validate_token(settings.SECRET_KEY, request.GET['state'].encode('UTF-8'), request.user):
		return  HttpResponseBadRequest()
	
	credential = FLOW.step2_exchange(request.GET)
	http = httplib2.Http()
	http = credential.authorize(http)
	service = build("gmail", "v1", http=http)
	try:
		label_object = {'messageListVisibility': "show",
           				'name': "IFP",
           				'labelListVisibility': "labelShow"}
		label = service.users().labels().create(userId='me',
												body=label_object).execute()
		print(label['id'])
	except errors.HttpError:
		print('An error occurred: %s' % error)
	storage = DjangoORMStorage(CredentialsModel, 'id', request.user, 'credential')
	storage.put(credential)
	return HttpResponseRedirect("/")