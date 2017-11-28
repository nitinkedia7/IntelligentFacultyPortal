from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^dept/(?P<pk>\d+)$', views.DepartmentDetail.as_view(), name='department-detail'),
	url(r'^dept/faculty/(?P<pk>\d+)$', views.FacultyDetail.as_view(), name='faculty-detail'),
	url(r'^accounts/signup/(?P<dept>\d+)$', views.SignUp, name='signup'),
	url(r'^accounts/login/$', auth_views.login, {'authentication_form' : LoginForm }, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, name='logout'),
	
	# url(r'^faculty/update/(?P<pk>\d+)$', views.FacultyUpdate.as_view(), name='faculty-update-profile'),
	url(r'^faculty/update/(?P<pk>\d+)$', views.UpdateFaculty, name='faculty-update-profile'),
	
	url(r'^faculty/add/course/(?P<pk>\d+)$', views.AddCourse, name='faculty-add-course'),
	url(r'^faculty/add/student/(?P<pk>\d+)$', views.AddStudent, name='faculty-add-student'),
	url(r'^faculty/add/conference/(?P<pk>\d+)$', views.AddConference, name='faculty-add-conference'),
	url(r'^faculty/add/journal/(?P<pk>\d+)$', views.AddJournal, name='faculty-add-journal'),
	url(r'^faculty/add/project/(?P<pk>\d+)$', views.AddProject, name='faculty-add-project'),
	url(r'^faculty/add/education/(?P<pk>\d+)$', views.AddEducation, name='faculty-add-education'),
	url(r'^faculty/add/achievement/(?P<pk>\d+)$', views.AddAchievement, name='faculty-add-achievement'),
	url(r'^faculty/add/professional_experience/(?P<pk>\d+)$', views.AddProfessionalExperience, name='faculty-add-professional-experience'),		
	url(r'^faculty/add/admin_responsibily/(?P<pk>\d+)$', views.AddAdministrativeResponsibility, name='faculty-add-administrative-responsibility'),
	
	url(r'^faculty/$', views.FacultyProfile, name='faculty-profile'),
	url(r'^dept/faculty/(?P<fac_id>[0-9]+)/(?P<attr_id>[0-9]+)$', views.FacultyAttributes, name='faculty-attributes'),
]