from atexit import register
import imp
from django.contrib import admin
from .models import *

admin.site.register(logger)
admin.site.register(employee_rating)
admin.site.register(model_rating)
admin.site.register(activity)
admin.site.register(projects)
admin.site.register(Employee)
admin.site.register(login_table)

# Register your models here.
