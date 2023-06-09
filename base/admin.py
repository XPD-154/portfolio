from django.contrib import admin
from .models import *

# Register your models here.
class InformationAdmin(admin.ModelAdmin):
  list_display = ("Summary", "about_us", "company_profile", "contact_us",)
admin.site.register(Information, InformationAdmin)

class SkillsAdmin(admin.ModelAdmin):
  list_display = ("name", "rating",)
admin.site.register(Skills, SkillsAdmin)

class ProjectsAdmin(admin.ModelAdmin):
  list_display = ("project_title", "project_description", "project_link", "project_type", "code_repo", "image",)
admin.site.register(Projects, ProjectsAdmin)

class Contact_usAdmin(admin.ModelAdmin):
  list_display = ("name", "email", "message",)
admin.site.register(Contact_us, Contact_usAdmin)