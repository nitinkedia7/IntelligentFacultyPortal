from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^dept/(?P<pk>\d+)$', views.DepartmentDetail.as_view(), name='dept_detail'),
]