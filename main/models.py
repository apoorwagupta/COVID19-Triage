from django.db import models
from multiselectfield import MultiSelectField
# Create your models here 
# We use models to store the data we want to store in thi smain app inthe backend.
#fields are list of table columns of database(mapping to a database). a field is instantiated as a class attribute and represents a particular table column.
class Patient(models.Model):
    name = models.CharField(max_length=50) #used to store text , max length is required.
    phone_num = models.CharField(max_length=15)
    patient_relative_name = models.CharField(max_length=50, null=True) #if a field has blank=True, form validation will allow entry of an empty value.
    patient_relative_contact = models.CharField(max_length=15, null=True) #NULL is for database, leave sthe column empty
    address = models.TextField()
    SYMPTOMS = (#choice fields
        ('Fever', 'Fever'), # specifying choices
        ('Dry cough', 'Dry cough'),
        ('Tiredness', 'Tiredness'),
        ('Aches and pains', 'Aches and pains'),
        ('Sore throat', 'Sore throat'),
        ('Diarrhoea', 'Diarrhoea'),
        ('Loss of taste or smell', 'Loss of taste or smell'),
        ('Difficulty in breathing or shortness of breath', 'Difficulty in breathing or shortness of breath'),
        ('Chest pain or pressure', 'Chest pain or pressure'),
        ('Loss of speech or movement', 'Loss of speech or movement'),
    )

    symptoms = MultiSelectField(choices=SYMPTOMS, null=True) # multiselect field to choose more than one choices.
    prior_ailments = models.TextField() #used to store large texts
    bed_num = models.ForeignKey("Bed", on_delete=models.CASCADE) # associating the bednum field with the bed model.
    dob = models.DateField(null=True) #used for dates  represented by date.datetime() instance.
    bed_num = models.ForeignKey("Bed", on_delete=models.CASCADE) # associating the doctor field with the doctor model.
    doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE, null=True)
    doctors_notes = models.TextField(null=True, blank=True) #for large text, default from widget is text area.
    doctors_visiting_time = models.CharField(null=True, max_length=50, blank=True)
    status = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name #returns our model name in the database as the name we entered in the form.
        
class Bed(models.Model):
    bed_number = models.CharField(max_length=50)
    occupied = models.BooleanField() #true/false input. default form widget is checkbox.
    def __str__(self):
        return self.bed_number


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):  
        return self.name


