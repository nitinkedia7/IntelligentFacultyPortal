from django.forms import ModelForm
from .models import Department, Designation, Faculty, Education, Course, Journal, Conference, ProfessionalExperience, Achievement, AdministrativeResponsibility, Student

class StudentForm(ModelForm):
	class Meta:
		model = Student
		exclude = ['faculty']

class FacultyForm(ModelForm):
	class Meta:
		model = Faculty
		exclude = ['user']
	
class EducationForm(ModelForm):
	class Meta:
		model = Education
		exclude = ['faculty']	

class CourseForm(ModelForm):
	class Meta:
		model = Course
		exclude = ['faculty']

class JournalForm(ModelForm):
	class Meta:
		model = Journal
		exclude = ['faculty']

class ConferenceForm(ModelForm):
	class Meta:
		model = Conference
		exclude = ['faculty']

class ProjectForm(ModelForm):
	class Meta:
		model = Education
		exclude = ['faculty']

class ProfessionalExperienceForm(ModelForm):
	class Meta:
		model = ProfessionalExperience
		exclude = ['faculty']

class AchievementForm(ModelForm):
	class Meta:
		model = Achievement
		exclude = ['faculty']

class AdministrativeResponsibilityForm(ModelForm):
	class Meta:
		model = AdministrativeResponsibility
		exclude = ['faculty']