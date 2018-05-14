from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib import admin
# Models for Gmail API 
from oauth2client.contrib.django_util.models import CredentialsField

class CredentialsModel(models.Model):
  id = models.ForeignKey(User, primary_key=True, on_delete=models.CASCADE)
  credential = CredentialsField()


class CredentialsAdmin(admin.ModelAdmin):
    pass
# Create your models here.

class Department(models.Model):
	DEPARTMENT = (
		('bsbe', "Biosciences and Bioengineering"),
		('chem', "Chemistry"),
		('ce', "Chemical Engineering"),
		('civil', "Civil Engineering"),
		('des', "Design"),
		('cse', "Computer Science and Engineering"),
		('eee', "Electronics and Electrical Engineering"),
		('hss', "Humanities and Social Sciences"),
		('phy', "Physics"),
		('math', "Mathematics"),
		('mech', "Mechanical Engineering"),
	)
	department = models.CharField(max_length=6, choices=DEPARTMENT)
	dept_pic = models.ImageField(upload_to="media/dept_pic", null=True, blank=True, help_text="Department Picture")
	dept_logo = models.ImageField(upload_to="media/dept_logo", null=True, blank=True, help_text="Department Logo")

	email = models.EmailField(max_length=254, default="@iitg.ernet.in", null=True)
	block = models.CharField(max_length=1, null=True)
	phone = models.CharField(max_length=15, default="+91-361-258XXXX", null=True)

	def __str__(self):
		return self.get_department_display()

	def get_absolute_url(self):
		return reverse('department-detail', args=[str(self.id)])

class Designation(models.Model):    
    DESIGNATION = (
		('asso', "Associate Professor"),
		('asst', "Assistant Professor"),
		('prof', "Professor"),
		('visf', "Visiting Professor"),
		('hono', "Honorary Professor"),
	)
    designation = models.CharField(max_length=4,choices=DESIGNATION)
    
    def __str__(self):
        return self.get_designation_display()

class Student(models.Model):
	faculty = models.ForeignKey('Faculty', on_delete=models.SET_NULL, null=True)

	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	topic = models.CharField(max_length=75)
	start_year= models.IntegerField(default=2016)
	end_year= models.IntegerField(default=2020)
	DEGREE = (
		('bt', "B.Tech"),
		('bs', "B.Sc"),
		('be', "B.E."),
		('mt', "M.Tech"),
		('ms', "M.Sc"),
		('ph', "Ph.D."),
	)
	degree = models.CharField(max_length=2, choices=DEGREE, null=True)

	def __str__(self):
		return '{0} {1}, {2}, {3}'.format(self.first_name, self.last_name, self.get_degree_display(), self.topic)

	def get_absolute_url(self):
		return reverse('faculty-detail', args=(self.faculty.id,))

class Faculty(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, related_name="faculty")
	
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	
	profile_picture = models.ImageField(upload_to="media/profile_pic", default="media/profile_pic/default_profile_pic.jpg", blank=True)
	residential_phone = models.CharField(max_length=15, default="+91-361-258XXXX", blank=True)
	office_phone = models.CharField(max_length=15, default="+91-361-258XXXX")
	iitg_email = models.EmailField("Primary Email", max_length=254, default="username@iitg.ernet.in")
	other_email = models.EmailField("Secondary Email", max_length=254, default="username@gmail.com", blank=True)
	room_number = models.CharField(max_length=5, default="H-000")
	designation = models.ForeignKey('Designation', on_delete=models.CASCADE, null=True)
	department = models.ForeignKey('Department', on_delete=models.CASCADE, null=True)

	interests = models.CharField(max_length=200, null=True)

	biography = models.CharField(max_length=1500, null=True)

	# Metadata
	class Meta:
		ordering = ["id"]
		verbose_name_plural = "Faculties"

	# Methods
	def get_absolute_url(self):
		return reverse('faculty-detail', args=(self.id,))

	def __str__(self):
		return '{0} {1}, {2}, {3}'.format(self.first_name, self.last_name, self.designation, self.department)

class Education(models.Model):
	faculty = models.ForeignKey('Faculty', on_delete=models.SET_NULL, null=True)
	DEGREE = (
		('bt', "Bachelor of Technology (B.Tech)"),
		('bs', "Bachelor of Science (B.Sc)"),
		('be', "Bachelor of Engineering (B.E.)"),
		('mt', "Master of Technology (M.Tech)"),
		('ms', "Master of Science (M.Sc)"),
		('ph', "Doctor of Philosophy (Ph.D."),
	)
	degree = models.CharField(max_length=2, choices=DEGREE)
	branch = models.CharField(max_length=50)
	institute = models.CharField(max_length=50)
	duration = models.CharField(max_length=7, default="XXXX-XX")
	
	class Meta:
		ordering = ["duration"]
		verbose_name_plural = "Education"
	
	def __str__(self):
		return '{0}, {1}'.format(self.get_degree_display(), self.branch)

class Course(models.Model):
    faculty = models.ForeignKey('Faculty', on_delete=models.SET_NULL, null=True)
    name = models.CharField('Course Name', max_length=50)
    code = models.CharField('Course Code', max_length=6, default="CS221")
    SEMESTER = (
        ('odd', "July-Nov"),
        ('even', "Jan-May"),
    )
    semester = models.CharField(max_length=4, choices=SEMESTER)
    year = models.IntegerField(default=2017)
    
    class Meta:
    	ordering = ["year"]
    	verbose_name_plural = "Courses"
    
    def __str__(self):
        return '{0}, {1}, {2}'.format(self.name, self.get_semester_display(), self.year)
    
    def get_absolute_url(self):
    	return reverse('faculty-detail', args=(self.faculty.id,))

class Journal(models.Model):
    faculty = models.ForeignKey('Faculty', on_delete=models.SET_NULL, null=True)   
    title = models.CharField(max_length=100)
    contributors = models.CharField(max_length=100)
    book = models.CharField('Published In', max_length=100)
    year = models.IntegerField(default=2017)

    class Meta:
    	ordering = ['year']
    
    def __str__(self):
    	return '{0}, {1}'.format(self.title, self.year)

class Conference(models.Model):
    faculty = models.ForeignKey('Faculty', on_delete=models.SET_NULL, null=True)
    participants = models.CharField(max_length=200)
    topic = models.CharField(max_length=100)
    event = models.CharField(max_length=200)
    year = models.IntegerField(default=2017)

    class Meta:
    	ordering = ['year']

    def __str__(self):
        return self.topic

class Project(models.Model):
    faculty = models.ForeignKey('Faculty', on_delete=models.SET_NULL, null=True)
   
    title = models.CharField(max_length=100, null=True)
    sponsor = models.CharField(max_length=50, null=True)
    budget = models.CharField(max_length=20, null=True)
    duration = models.CharField(max_length=7, default="20XX-XX", null=True)
    role = models.CharField(max_length=30, null=True)

    class Meta:
    	ordering = ['duration']

    def __str__(self):
        return '{0}, {1}'.format(self.title, self.duration)

# class ResearchInterest(models.Model):
#     faculty = models.ForeignKey('Faculty', on_delete=models.SET_NULL, null=True)
#     interests = models.CharField(max_length=200, help_text="Enter your interests separated by commas")
#     def __str__(self):
#         return self.interests

class ProfessionalExperience(models.Model):
	faculty = models.ForeignKey('Faculty', on_delete=models.SET_NULL, null=True)
	designation = models.CharField(max_length=50)
	institute = models.CharField(max_length=200)
	duration = models.CharField(max_length=20, default="2017-Ongoing")

	class Meta:
		ordering = ['duration']
	def __str__(self):
		return '{0}, {1}'.format(self.designation, self.institute)

class Achievement(models.Model):
	faculty = models.ForeignKey('Faculty', on_delete=models.SET_NULL, null=True)
	award = models.CharField(max_length=200)
	awarded_by = models.CharField(max_length=200)
	year = models.IntegerField(default=2017)

	class Meta:
		ordering = ['year']
	
	def __str__(self):
		return '{0}, {1}'.format(self.award, self.year)

class AdministrativeResponsibility(models.Model):
	faculty = models.ForeignKey('Faculty', on_delete=models.SET_NULL, null=True)
	designation = models.CharField(max_length=50)
	
	start = models.CharField('From', max_length=20, default="Jan 2017")
	end = models.CharField('Till', max_length=20, default="Present", blank=True)
	
	class Meta:
		verbose_name_plural = "Administrative Responsibilities"

	def __str__(self):
		return "{0}, {1} to {2}".format(self.designation, self.start, self.end)