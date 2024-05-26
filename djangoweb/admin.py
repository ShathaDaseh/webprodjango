from django.contrib import admin
from .models import *

admin.site.register(Students)
admin.site.register(studentsReg)
admin.site.register(Courses)
admin.site.register(CourseSchedules)
admin.site.register(CoursePrerequisite)