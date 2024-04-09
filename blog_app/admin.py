from django.contrib import admin
from .import models



admin.site.register(models.Catagory)
admin.site.register(models.Article)

admin.site.register(models.Comment)

admin.site.register(models.Messagee)
