from django.contrib import admin

# Register your models here.
from .models import Department, Designation, Faculty, Education, Course, Journal, Conference, ProfessionalExperience, Achievement, AdministrativeResponsibility, Student


admin.site.register(Department)
admin.site.register(Designation)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Education)
admin.site.register(Course)
admin.site.register(Journal)
admin.site.register(Conference)
admin.site.register(ProfessionalExperience)
admin.site.register(Achievement)
admin.site.register(AdministrativeResponsibility)