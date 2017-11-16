from django.conf.urls import url, include

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^dept/(?P<pk>\d+)$', views.DepartmentDetail.as_view(), name='department-detail'),
	url(r'^dept/faculty/(?P<pk>\d+)$', views.FacultyDetail.as_view(), name='faculty-detail'),
	url(r'^accounts/signup$', views.SignUp, name='signup'),
	url(r'^faculty/create/$', views.FacultyCreate.as_view(), name='info'),
	url(r'^faculty/$', views.FacultyProfile, name='faculty-detail'),
	url(r'^dept/faculty/(?P<pk>\d+)/teaching$', views.FacultyTeaching, name='faculty-teaching'),
	url(r'^dept/faculty/(?P<pk>\d+)/about$', views.FacultyAbout, name='faculty-about'),
	url(r'^dept/faculty/(?P<pk>\d+)/publications$', views.FacultyPublications, name='faculty-publications'),
	url(r'^dept/faculty/(?P<fac_id>[0-9]+)/(?P<attr_id>[0-9]+)$', views.FacultyAttributes, name='faculty-attributes'),
]