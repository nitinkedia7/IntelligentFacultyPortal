from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.forms import ModelForm
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

class Faculty(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
	
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	
	profile_picture = models.ImageField(upload_to="media/profile_pic", blank=True)
	residential_phone = models.CharField(max_length=15, default="+91-361-258XXXX", blank=True)
	office_phone = models.CharField(max_length=15, default="+91-361-258XXXX")
	iitg_email = models.EmailField("IITG Webmail", max_length=254, default="@iitg.ernet.in")
	other_email = models.EmailField("Secondary Email", max_length=254, blank=True)
	room_number = models.CharField(max_length=5, default="H-000")
	designation = models.ForeignKey('Designation', on_delete=models.PROTECT, null=True)
	department = models.ForeignKey('Department', on_delete=models.PROTECT, null=True)

	# Metadata
	class Meta:
		ordering = ["-id"]
		verbose_name_plural = "Faculties"

	# Methods
	def get_absolute_url(self):

		return reverse('faculty-detail', args=[str(self.id)])

	def __str__(self):

		return '{0} {1}'.format(self.first_name, self.last_name)

class Education(models.Model):

	faculty = models.ForeignKey('Faculty', on_delete=models.SET_NULL, null = True)
	DEGREE = (
		('bt', "B.Tech"),
		('bs', "B.Sc"),
		('be', "B.E"),
		('mt', "M.Tech"),
		('ms', "M.Sc"),
		('ph', "PhD"),
	)
	degree = models.CharField(max_length=2, choices=DEGREE, help_text='Degree obtained')
	branch = models.CharField(max_length=50, help_text="Enter full name of the Discipline")
	institute = models.CharField(max_length=50, help_text="Enter full name of the Institute")
	duration = models.CharField(max_length=7, help_text="Please use the following format: <em>XXXX-XX</em>")

	def __str__(self):
		return self.degree

	class Meta:
		verbose_name_plural = "Education"	

class Course(models.Model):
    faculty = models.ForeignKey('Faculty', on_delete=models.SET_NULL, null = True)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5, help_text="eg. MA101")
    SEMESTER = (
        ('odd', "July-Nov"),
        ('even', "Jan-March"),
    )
    semester = models.CharField(max_length=4, choices=SEMESTER)
    year = models.IntegerField()
    
    def __str__(self):
        return self.name

class Journal(models.Model):
    faculty = models.ForeignKey('Faculty', on_delete=models.SET_NULL, null = True)   
    title = models.CharField(max_length=100, help_text="Enter title of Journal")
    contributors = models.CharField(max_length=100, help_text="Enter names of all contributors")
    book = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.title

class Conference(models.Model):
    faculty = models.ForeignKey('Faculty', on_delete=models.SET_NULL, null = True)
    participants = models.CharField(max_length=200, help_text="Enter names of all participants separated by commas")
    topic = models.CharField(max_length=1000)
    event = models.CharField(max_length=200, help_text="Enter name of event and place where hosted")
    year = models.IntegerField()

    def __str__(self):
        return self.topic

class ResearchInterest(models.Model):
    faculty = models.ForeignKey('Faculty', on_delete=models.SET_NULL, null = True)
    interests = models.CharField(max_length=200, help_text="Enter your interests separated by commas")
    def __str__(self):
        return self.interests

class ProfessionalExperience(models.Model):
	faculty = models.ForeignKey('Faculty', on_delete=models.SET_NULL, null = True)
	designation = models.CharField(max_length=50)
	institute = models.CharField(max_length=200)
	start_year = models.IntegerField()
	end_year = models.IntegerField()

	def __str__(self):
		return '{0}, {1}'.format(self.designation, self.institute)

class Achievement(models.Model):
	faculty = models.ForeignKey('Faculty', on_delete=models.SET_NULL, null = True)
	award = models.CharField(max_length=200)
	awarded_by = models.CharField(max_length=200)
	year = models.IntegerField()

	def __str__(self):
		return '{0}, {1}'.format(self.award, self.year)

class AdministrativeResponsibility(models.Model):
	faculty = models.ForeignKey('Faculty', on_delete=models.SET_NULL, null = True)
	designation = models.CharField(max_length=50)
	start_month = models.CharField(max_length=50)
	start_year = models.IntegerField()
	end_month = models.CharField(max_length=50)
	end_year = models.IntegerField()

	def __str__(self):
		return self.designation

	class Meta:
		verbose_name_plural = "AdministrativeResponsibility"	