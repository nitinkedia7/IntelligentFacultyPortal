from django.conf.urls import url, include

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^dept/(?P<pk>\d+)$', views.DepartmentDetail.as_view(), name='department-detail'),
	url(r'^dept/faculty/(?P<pk>\d+)$', views.FacultyDetail.as_view(), name='faculty-detail'),
	url(r'^accounts/signup$', views.SignUp, name='signup'),
	
	url(r'^faculty/update/(?P<pk>\d+)$', views.FacultyUpdate.as_view(), name='faculty-update-profile'),

	url(r'^faculty/add/course/(?P<pk>\d+)$', views.CourseCreate.as_view(), name='faculty-create-course'),
	url(r'^faculty/add/student/(?P<pk>\d+)$', views.AddStudent, name='faculty-create-student'),
	
	url(r'^faculty/$', views.FacultyProfile, name='faculty-profile'),
	url(r'^dept/faculty/(?P<fac_id>[0-9]+)/(?P<attr_id>[0-9]+)$', views.FacultyAttributes, name='faculty-attributes'),
	# url(r'^accounts/add_detail/$', views.FacultyUpdate, name='faculty-update-profile'),
]