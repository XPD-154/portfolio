from django.db import models

# Create your models here.
class Information(models.Model):
    Summary = models.TextField(null=True)
    about_us = models.TextField(null=True)
    company_profile = models.TextField(null=True)
    contact_us = models.TextField(null=True)
    
class Skills(models.Model):
    name = models.CharField(max_length=200, null=True)
    rating = models.CharField(max_length=200, null=True)
    
class Projects(models.Model):
    project_title = models.CharField(max_length=200, null=True)
    project_description = models.TextField(null=True)
    project_link = models.CharField(max_length=200, null=True)
    project_type = models.CharField(max_length=200, null=True)
    code_repo = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)

    #method to account for image error
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
class Contact_us(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    message = models.TextField(null=True)