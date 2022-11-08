from django.db import models

# Create your models here.
class PersonalInformation(models.Model):
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Middle  = models.CharField(max_length=20)
    Other_Names_Used = models.CharField(max_length=20)
    Primary_Phone = models.CharField()
    Secondary_Phone = models.CharField()
    Mailing_Address = models.CharField(help_text='Box # or Street Address', default='Hello')
    Physical_Address = models.CharField(help_text='Rural or Residential', default='Hello')
