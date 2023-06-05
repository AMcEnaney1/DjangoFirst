from django.contrib import admin
from projects.models import Project


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project)
from django.contrib import admin

# Register your models here.
