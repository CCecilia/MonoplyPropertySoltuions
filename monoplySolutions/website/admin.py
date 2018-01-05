__author__ = 'christian.cecilia1@gmail.com'
from django.contrib import admin
from .models import *

admin.site.register(Company)
admin.site.register(Service)
admin.site.register(Job)
admin.site.register(JobCategory)
admin.site.register(TeamMember)