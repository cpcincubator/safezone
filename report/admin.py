from django.contrib import admin

# Register your models here.
from .models import Report,Contact

admin.site.register(Report)
admin.site.register(Contact)