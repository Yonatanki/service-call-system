from django.contrib import admin

# Register your models here.
from .models import category, location, department, employee, sub_category, call_request, status, status_request, message, privileges

admin.site.register(category)
admin.site.register(location)
admin.site.register(department)
admin.site.register(employee)
admin.site.register(sub_category)
admin.site.register(call_request)
admin.site.register(status)
admin.site.register(status_request)
admin.site.register(message)
admin.site.register(privileges)