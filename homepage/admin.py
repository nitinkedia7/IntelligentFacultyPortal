from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Course, Journal, Conference, Research_Interest

admin.site.register(Course)
admin.site.register(Journal)
admin.site.register(Conference)
admin.site.register(Research_Interest)

from django.contrib import admin

from .models import ProfessionalExperience
from .models import Achievement
from .models import AdministrativeResponsibilty

admin.site.register(ProfessionalExperience)
admin.site.register(Achievement)
admin.site.register(AdministrativeResponsibilty)

