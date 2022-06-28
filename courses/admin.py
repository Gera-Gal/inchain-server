from msilib.schema import Media
from django.contrib import admin

from .models import MediaFile, Course

admin.site.register(MediaFile)
admin.site.register(Course)