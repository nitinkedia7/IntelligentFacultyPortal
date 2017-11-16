from django.conf.urls import url, include

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^dept/(?P<pk>\d+)$', views.DepartmentDetail.as_view(), name='department-detail'),
	url(r'^accounts/signup$', views.SignUp, name='signup'),
	url(r'^faculty/create/$', views.FacultyCreate.as_view(), name='info'),
]