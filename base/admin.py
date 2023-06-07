from django.contrib import admin
from .models import *

# Register your models here.
class InformationAdmin(admin.ModelAdmin):
  list_display = ("Summary", "about_us", "company_profile", "contact_us",)
admin.site.register(Information, InformationAdmin)

class SkillsAdmin(admin.ModelAdmin):
  list_display = ("name",)
admin.site.register(Skills, SkillsAdmin)

class ProjectsAdmin(admin.ModelAdmin):
  list_display = ("project_title", "project_description", "project_link", "code_repo", "image",)
admin.site.register(Projects, ProjectsAdmin)