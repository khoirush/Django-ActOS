from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.http import request, HttpRequest


class PersonnelForm (ModelForm):
    class Meta:
        model = Personnel
        fields = ['ID_Personnel', 'First_Name',
                  'Last_Name', 'Position', 'Status']


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['ID_Customer', 'Customer_Name']


class VendorForm(ModelForm):
    class Meta:
        model = Vendor
        fields = ['ID_Vendor', 'Vendor_Name']


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['Title',
                  'Description', 'Start_Date', 'End_Date']
        widgets = {
            'Description': forms.Textarea,
        }


class ProjectTaskForm(ModelForm):
    class Meta:
        model = ProjectTask
        fields = ['Title', 'Priority', 'Description', 'Status',
                  'PctComplete', 'PctWeight', 'Start_Date', 'TargetFinish_Date', 'PIC'
                  ]


class ProjectAssignmentForm(ModelForm):
    class Meta:
        model = ProjectAssignment
        fields = ['ID_Personnel',
                  'is_PM', 'Start_Date', 'End_Date']
        label = ['Personnel', 'as a PM ?', 'Start_Date', 'End_Date']


class ActivityLogForm(ModelForm):
    class Meta:
        model = ActivityLog
        fields = ['Activity_Date',
                  'ID_Assignment', 'ID_ProjectTask', 'Location', 'Description']

    # def __init__(self, *args, **kwargs):
    #     super(ActivityLogForm, self).__init__(*args, **kwargs)
    #     personnel = UserPersonnel.objects.get(ID_User=HttpRequest.user)
    #     projects = ProjectAssignment.objects.filter(ID_Personnel=personnel)
    #     tasks = ProjectTask.objects.filter(ID_Projects=projects)
    #     self.fields['ID_ProjectTask'].queryset = tasks

# class DetailActivityForm(ModelForm):
#     class Meta:
#         model = DetailActivity
#         fields = ['ID_ProjectTask', 'ID_Activity',
#                   'Description', 'Location', 'PctTaskComplete']
