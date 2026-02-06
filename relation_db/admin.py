from django.contrib import admin
from . import models


admin.site.register(models.Tag)
admin.site.register(models.Person)
admin.site.register(models.Tour)
admin.site.register(models.Review)
# Register your models here.
