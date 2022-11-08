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
    Chapter_House = models.CharField(help_text='Kayenta', default='Chapter House', max_length=30)
    choices = [
        ('yes', 'yes'),
        ('no', 'no'),
        ]
    Veteran = models.CharField(choices=choices, max_length=3)
    marital_status = [
        ('1', 'single'),
        ('2', 'Married'),
        ('3', 'Separated'),
        ('4', 'Widowed'),
        ('5', 'Divorced'),
        ('6', 'Common Law'),
    ]
    Marital_Status = models.CharField(max_length=15, default='Single', choices=marital_status)
    Languages = [
        ('English', 'English'),
        ('Navajo', 'Navajo'),
        ('Both', 'Both'),
        ('Other', 'Other'),
    ]
    Languages_Spoken = models.CharField(max_length=10, choices=Languages)
    Time_at_Residence = models.IntegerField(max_length=2, help_text='years')

class householdMem(models.Model):
    First_Name = models.CharField()
    Last_Name = models.CharField()
    Social_Security_Number = models.CharField()
    Tribal_Enrollment_Number = models.IntegerField()
    Date_of_Birth = models.IntegerField() # I need to figure out how to create a nicer model for DOB and Length of stay
    relation = [
        ('self', 'self'),
        ('sister', 'sister'),
        ('brother', 'brother'),
        ('mother', 'mothers'),
        ('father', 'father'),
        ('nephew', 'nephew'),
        ('niece', 'niece'),
        ('grandmother', 'grandmother'),
        ('grandfather', 'grandfather'),

    ]
    Relation_to_Applicant = models.CharField(max_length=13, choices=relation)
    choices = [
        ('yes', 'yes'),
        ('no', 'no'),
    ]
    US_Citizen = models.CharField(max_length=3, choices=choices)
    Ethnicity = models.CharField(max_length=25)
    gender = [
        ('m', 'male'),
        ('f', 'female'),
    ]
    Gender = models.CharField(max_length=3, choices=gender)

    gradelevel = [
        ('1', 'Less than high school'),
        ('2', 'High school diploma or equivalent'),
        ('3', 'Some college, no degree'),
        ('4', 'Postsecondary non-degree award'),
        ('5', 'Associate’s degree'),
        ('6', 'Bachelor’s degree'),
        ('7', 'Master’s degree'),
        ('8', 'Doctoral or professional degree'),
    ]
    Last_Grade_Completed = models.CharField(choices=gradelevel, default=5)

    Have_Received_TANF_Before = models.CharField(max_length=2, default='no', choices=choices)
    fiftystates = [
         ("Alabama", "Alabama"),
         ("Alaska", "Alaska"),
         ("Arizona", "Arizona"),
         ("Arkansas", "Arkansas"),
         ("California", "California"),
         ("Colorado", "Colorado"),
         ("Connecticut", "Connecticut"),
         ("Delaware", "Delaware"),
         ("Florida", "Florida"),
         ("Georgia", "Georgia"),
         ("Hawaii", "Hawaii"),
         ("Idaho", "Idaho"),
         ("Illinois", "Illinois"),
         ("Indiana", "Indiana"),
         ("Iowa", "Iowa"),
         ("Kansas", "Kansas"),
         ("Kentucky", "Kentucky"),
         ("Louisiana", "Louisiana"),
         ("Maine", "Maine"),
         ("Maryland", "Maryland"),
         ("Massachusetts", "Massachusetts"),
         ("Michigan", "Michigan"),
         ("Minnesota", "Minnesota"),
         ("Mississippi", "Mississippi"),
         ("Missouri", "Missouri"),
         ("Montana", "Montana"),
         ("Nebraska", "Nebraska"),
         ("Nevada", "Nevada"),
         ("New Hampshire", "New Hampshire"),
         ("New Jersey", "New Jersey"),
         ("New Mexico", "New Mexico"),
         ("New York", "New York"),
         ("North Carolina", "North Carolina"),
         ("North Dakota", "North Dakota"),
         ("Ohio", "Ohio"),
         ("Oklahoma", "Oklahoma"),
         ("Oregon", "Oregon"),
         ("Pennsylvania", "Pennsylvania"),
         ("Rhode Island", "Rhode Island"),
         ("South Carolina", "South Carolina"),
         ("South Dakota", "South Dakota"),
         ("Tennessee", "Tennessee"),
         ("Texas", "Texas"),
         ("Utah", "Utah"),
         ("Vermont", "Vermont"),
         ("Virginia", "Virginia"),
         ("Washington", "Washington"),
         ("West Virginia", "West Virginia"),
         ("Wisconsin", "Wisconsin"),
         ("Wyoming", "Wyoming")
        ]
    If_Yes_What_State = models.CharField(default='California', choices=fiftystates)
    How_long_did_recieve_TANF = models.IntegerField(default='years', help_text='years')
    Months_received_TANF = models.IntegerField(default='months', help_text='months')
    Have_you_ever_been_disqualified_from_TANF = models.CharField(choices=choices)
    Explain_Disqualification = models.TextField()
    Are_you_or_anyone_in_the_household_on_probation_or_parole = models.CharField(choices=choices)
    Are_conditions_of_parole_being_met = models.CharField(choices=choices)
    Do_you_or_anyone_in_the_household_have_an_outstanding_warrant = models.CharField(choices=choices)
    Is_anyone_in_the_household_attending_school = models.CharField(choices=choices)
    Students_name = models.CharField(max_length=25, default='students name')
    Schools_Name = models.CharField(max_length=25, default='school name')
    Address = models.CharField(max_length=100, default='address')
    Last_Grade_Completed = models.CharField(choices=gradelevel, default=5)
    status = [
        ('FT', 'Full Time'),
        ('PT', 'Part Time'),
    ]
    Full_or_Part_Time = models.CharField(choices=status)
    Child_Support_Payments = models.CharField(choices=choices)
    SSB_Retirement_Survivors_Disability = models.CharField(choices=choices)
    Retirement_Federal_State_Tribal_RR = models.CharField(choices=choices)
    Royalty_Payments = models.CharField(help_text='oil/gas/etc', choices=choices)
    Rental_Lease_of_Property = models.CharField(c)

