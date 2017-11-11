from django.db import models

# Create your models here.

class Designation(models.Model)
	POST = (
		('asso', "Associate Professor"),
		('asst', "Assistant Professor"),
		('prof', "Professor"),
		('visf', "Visiting Professor"),
		('hono', "Honorary Professor"),
	)
	post = models.CharField(max_length=4, choices=POST)

	DEPARTMENT = (
		('bsbe', "Biosciences and Bioengineering"),
		('chem', "Chemistry"),
		('ce', "Chemical Engineering"),
		('cive', "Civil Engineering"),
		('des', "Design"),
		('cse', "Computer Science and Engineering"),
		('eee', "Electrical and Electronics Engineering"),
		('ece', "Electrical and Communication Engineering"),
		('hss', "Humanities and Social Sciences"),
		('phy', "Physics")
		('math', "Mathematics")
		('mech', "Mechanical Engineering")
	)
	department = models.CharField(max_length=4, choices=DEPARTMENT)


class basic_info(models.Model):
    """
    A class for storing personal information of the user
    """

    # Fields
    first_name = models.CharField(max_length=20, help_text="Enter First name")
    last_name = models.CharField(max_length=20, help_text="Enter Last name")
    
    phone_res = models.CharField(max_length=15, help_text="Please use the following format: <em>+91-361-258XXXX</em>.", default="+91-361-258XXXX")
    phone_office = models.CharField(max_length=15, help_text="Please use the following format: <em>+91-361-258XXXX</em>.", default="+91-361-258XXXX")
    
    iitg_webmail = models.EmailField(max_length=254, help_text="Please use the following format: <em>username@iitg.ernet.in</em>.", default="@iitg.ernet.in")
    other_email = models.EmailField(max_length=254, help_text="Please use the following format: <em>username@company.com</em>.")

    room_number = models.CharField(max_length=5, help_text="Please use the following format: X-XXX")

    designation = models.ForeignKey('Designation', help_text ="Add your current designation")


    # Metadata
    class Meta: 
        ordering = ["-last_name"]

    # Methods
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.field_name

class Education(models.Model):

	DEGREE = (
		('bt', "Bachelor of Technology"),
		('bs', "Bachelor of Science"),
		('be', "Bachelor of Engineering"),
		('mt', "Master of Technology"),
		('ms', "Master of Science"),
		('ph', "Post Doctorate"),
	)

	degree = models.CharField(max_length=2, choices=DEGREE, help_text='Degree obtained')

	branch = models.CharField(max_length=50, help_text="Enter full name of the Discipline")

	institute = models.CharField(max_length=50, help_text="Enter full name of the Institute")

	duration = models.CharField(max_length=7, help_text="Please use the following format: <em>XXXX-XX</em>")

from django.db import models

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Course(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    # Author as a string rather than object because it hasn't been declared yet in the file.
    session = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class Journal(models.Model):    
	name = models.CharField(max_length=100, help_text="Enter title of Journal")
	summary = models.TextField(max_length=1000, help_text="Enter a brief description of the Journal")

	# def __str__(self):
 #    	return self.name

class Conference(models.Model):
	names = models.CharField(max_length=200, help_text="Enter names of all participants separated by commas")
	topic = models.CharField(max_length=1000)
	event = models.CharField(max_length=200, help_text="Enter name of event and place where hosted")
	session = models.DateField(null=True, blank=True)

	# def __str__(self):
 #    	return self.topic

class Research_Interest(models.Model):
	names = models.CharField(max_length=200, help_text="Enter upto 5 interests separated by commas")

	# def __str__(self):
 #    	return self.names


from django.db import models

class ProfessionalExperience(models.Model):


	time = models.DateField(auto_now=False, auto_now_add=False)
	jobtitle = models.CharField(max_length=200)
	institutename = models.CharField(max_length=200)

	def __str__(self):
		return '%s, %s, %s' % (self.jobtitle, self.time, self.institutename)

class Achievement(models.Model):

	award = models.CharField(max_length=200)
	year = models.DateField(auto_now=False, auto_now_add=False)
	awardedby = models.CharField(max_length=200)

	def __str__(self):
		return '%s, %s, %s' % (self.award, self.year, self.awardedby)

class AdministrativeResponsibilty(models.Model):

	time = models.DateField(auto_now=False, auto_now_add=False)
	Designation = models.CharField(max_length=200)
	def __str__(self):
		return '%s, %s' % (self.Designation, self.time)