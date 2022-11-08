# import django.contrib.admin.filters
import django_filters
from .models import *

# ModelnameFilter
class PatientFilter(django_filters.FilterSet):          #allows users to filter down a queryset based on a model’s fields, displaying the form to let them do this.
    class Meta:                                         #meta class is used to specify multiple filters, i.e it will generate exact search for all the given fields
        model = Patient
        # fields = ['name', 'bed_num', 'status']
        fields = '__all__'
        exclude = ['phone_num', 'address', 'prior_ailments', 'dob', 'patient_relative_name', 'patient_relative_contact', 'symptoms', 'doctors_visiting_time', 'doctors_notes']
        
