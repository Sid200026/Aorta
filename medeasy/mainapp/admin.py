from django.contrib import admin
from .models import Patient,Doctor,ModelReport,ModelTwoReport, Notifications
# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(ModelReport)
admin.site.register(ModelTwoReport)
admin.site.register(Notifications)