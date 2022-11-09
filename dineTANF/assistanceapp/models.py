from django.db import models

# Create your models here.
class PersonalInformation(models.Model):
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Middle  = models.CharField(max_length=20)
    Other_Names_Used = models.CharField(max_length=20)
    Primary_Phone = models.IntegerField()
    Secondary_Phone = models.IntegerField()
    Mailing_Address = models.CharField(max_length=30, help_text='Box # or Street Address', default='Hello')
    Physical_Address = models.CharField(max_length=30, help_text='Rural or Residential', default='Hello')
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
        ('6', 'Common Law Marriage'),
    ]
    Marital_Status = models.CharField(max_length=15, default='Single', choices=marital_status)
    Languages = [
        ('English', 'English'),
        ('Navajo', 'Navajo'),
        ('Both', 'Both'),
        ('Other', 'Other'),
    ]
    Languages_Spoken = models.CharField(max_length=10, choices=Languages)
    Time_at_Residence = models.IntegerField(help_text='years')

class householdMem(models.Model):
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Social_Security_Number = models.CharField(max_length=9)
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
    Last_Grade_Completed = models.CharField(max_length=30, choices=gradelevel, default=5)

    Have_Received_TANF_Before = models.CharField(max_length=3, default='no', choices=choices)
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
    If_Yes_What_State = models.CharField(max_length=15, default='California', choices=fiftystates)
    How_long_did_recieve_TANF = models.IntegerField(default='years', help_text='years')
    Months_received_TANF = models.IntegerField(default='months', help_text='months')
    disqualified = models.CharField(max_length=3, choices=choices, verbose_name='Have you ever been disqualified from TANF?')
    Explain_Disqualification = models.TextField()
    Are_you_or_anyone_in_the_household_on_probation_or_parole = models.CharField(max_length=30, choices=choices)
    Are_conditions_of_parole_being_met = models.CharField(max_length=30, choices=choices)
    Do_you_or_anyone_in_the_household_have_an_outstanding_warrant = models.CharField(max_length=30, choices=choices)
    Is_anyone_in_the_household_attending_school = models.CharField(max_length=30, choices=choices)
    Students_name = models.CharField(max_length=25, default='students name')
    Schools_Name = models.CharField(max_length=25, default='school name')
    Address = models.CharField(max_length=100, default='address')
    Last_Grade_Completed = models.CharField(max_length=30, choices=gradelevel, default=5)
    status = [
        ('FT', 'Full Time'),
        ('PT', 'Part Time'),
    ]
    Full_or_Part_Time = models.CharField(max_length=2, choices=status)
    caliprice = [
        ('yes', 'yes'),
        ('no', 'no'),
        ('pending','pending'),
    ]
    Child_Support_Payments = models.CharField(max_length=7, choices=caliprice)
    #if choices == 'yes' or choices == 'pending':
     #   Recipient = models.TextField()
    #else:
     #   pass I tried adding a

    SSB_Retirement_Survivors_Disability = models.CharField(max_length=7, choices=choices)
    Retirement_Federal_State_Tribal_RR = models.CharField(max_length=7, choices=choices)
    Royalty_Payments = models.CharField(max_length=7, help_text='oil/gas/etc', choices=choices)
    Rental_Lease_of_Property = models.BooleanField(choices=caliprice)
    Capita = models.BooleanField(choices=caliprice, verbose_name='Per capita payments')
    Unemployment = models.CharField(max_length=7, choices=caliprice, verbose_name='Unemployment Insurance Comp')
    Vacation = models.BooleanField(max_length=7, choices=caliprice, verbose_name='Vacation/Sick/Severance Payments')
    Lottery = models.BooleanField(max_length=7, choices=caliprice, verbose_name='Lottery/Gambling Winnings')
    Insurance = models.CharField(max_length=7, choices=caliprice, verbose_name='Insurance/Settlement')
    Workers_Comp = models.CharField(max_length=7, choices=caliprice, verbose_name='Workers Compensation')
    Disability = models.CharField(max_length=7, choices=caliprice, verbose_name='Disablity Payments')
    Other = models.TextField(choices=caliprice)
    self_employed = models.CharField(max_length=7, choices=choices, verbose_name='Are you or anyone in your household currently self-employed?')
    type_of_employment = models.CharField(max_length=7, verbose_name='Type of Employement/Business Name')
    How_long = models.IntegerField()
    Hours_per_work = models.IntegerField()
    Monthly_Gross_Income = models.IntegerField()
    Monthly_Businesses_Expenses = models.IntegerField()
    Anyone_else_employed =  models.CharField(max_length=7, choices=choices, verbose_name='Is anyone in your household currently employed by others')
    Name = models.CharField(max_length=25, default='Name')
    Employers_address = models.CharField(max_length=50)
    Dates_of_Employement = models.DateField()
    Hours_per_week = models.IntegerField()
    Monthly_Gross_Income = models.IntegerField()
    Checking_Account = models.CharField(max_length=3, choices=choices)
    Savings_Account = models.CharField(max_length=3, choices=choices)
    Snap_Benefits = models.CharField(max_length=3, choices=choices, verbose_name='Does anyone in your household receive SNAP (food stamps)?')
    Subsidized_Housing = models.CharField(max_length=3, choices=choices, verbose_name='Are you receiving housing assistance(subsidized)?')
    Child_Care = models.CharField(max_length=3, choices=choices, verbose_name='Are you receiving child care assistance(subsidized)?')
    medical_benefits = [
        ('Medicaid', 'Medicaid'),
        ('Medicare', 'Medicare'),
        ('AZ AHCCCS', 'AZ AHCCCS'),
        ('Other Medical Coverage', 'Other Medical Coverage'),
    ]
    benefits = models.CharField(max_length=30, verbose_name='Does anyone in your household have: ', choices=medical_benefits)
    states = [
        ('AZ', 'Arizona'),
        ('UT', 'Utah'),
        ('NM', 'New Mexico')
    ]
    If_yes = models.CharField(max_length=2, verbose_name='If yes, from which state?', choices=states)
class acknowledgement(models.Model):
    choices = [
        ('yes', 'yes'),
        ('no', 'no'),
    ]
    Customer_responsibility = models.CharField(max_length=3, verbose_name='I understand and acknowledge I am responsible for providing complete and accurate information, reporting all the changes that may affect my eligibility for DSR assistance within five (5) business days after the change occurs, and cooperating with DSR staff, including, if necessary, investigations.', choices=choices)
    Personal_Responsibility_Plan = models.CharField(max_length=3, verbose_name='I understand I am required to develop a "Personal Responsibility Plan" (PRP) within thirty (30) days after approval for DSR assistance, comply with the provisions outlined in my PRP, and review my PRP with my assigned DSR staff at least once every 4 (4) months.', choices=choices)
    Work_Participation_Hours_Requirements = models.CharField(max_length=3, choices=choices, verbose_name='I understand adults included in a DSR assistance benefit group are required to participate in authorized work activities for a minimum number of hours each month. I understand that, if I am required to meet WPH requirements and do not meet the minimum hours, I will be subject to penalty. The types of work activities that are countable and the minimum number of hours I must participate have been explained to me.')
    Fair_Hearing_Rights = models.CharField(max_length=3, choices=choices, verbose_name='I understand if I do not agree with a decision made on my application or assistance case, I have a right to appeal the decision by submitting a request for Appeal Hearing within twenty(20) business days from the postmark date on the notice.')
    Confidentiality = models.CharField(max_length=3, choices=choices, verbose_name='I understand information obtained to determine my eligibility is confidential and, in compliance with the Navajo Nation Privacy and Access to Information Act, may not be released to a third party, unless I sign a Notarized release of Information form authorizing the release the information I have provided to the third party.')
    Release_of_Information = models.CharField(max_length=3, choices=choices, verbose_name='I authorize DSR to contact any other agency to obtain information necessary to determine my benfit groups eligibility for DSR assistance/benefits. I also authorize DSR to access my information stored in the DSR database to verify information I have provided and to prevent duplication of assistance.')
    Fraud_Penalties = models.CharField(max_length=3, choices=choices, verbose_name='I understand if I intentionally provide false information, or withold information, in order to make my benefit group eligible for DSR assistance or benefits we would otherwise be ineligible to receive, I and all members of my benefit group may be disqualified from receiving DSR assistance and benefits and required to repay any payments I was not eligible to receive. In addition, I may be subject to criminal penalties under applicable tribal, state, or federal laws.')
    Payment_Errors = models.CharField(max_length=3, choices=choices, verbose_name='I understand a payment error will occur if I receive a montly assistance payment that is more or less than I am eligible to receive. If I receive a payment for more or less than I was eligible to receive, I will immediately report this to the DSR. I understand I will responsible for repaying the amount I was not eligible to receive.')
    date_of_application = models.DateTimeField(auto_now_add=True, auto_created=True)









