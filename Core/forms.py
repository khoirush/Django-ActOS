from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.admin.widgets import AdminDateWidget


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
            'Start_Date': forms.SelectDateWidget,
            'End_Date': forms.SelectDateWidget
        }


class ProjectTaskForm(ModelForm):
    class Meta:
        model = ProjectTask
        fields = ['ID_Task', 'ID_Project', 'Title', 'Priority', 'Description', 'Status',
                  'PctComplete', 'PctWeight', 'Start_Date', 'TargetFinish_Date', 'PIC'
                  ]


class ProjectAssignmentForm(ModelForm):
    class Meta:
        model = ProjectAssignment
        fields = ['ID_Assignment', 'ID_Personnel',
                  'ID_Project', 'is_PM', 'Start_Date', 'End_Date']


class ActivityLogForm(ModelForm):
    class Meta:
        model = ActivityLog
        fields = ['ID_Activity', 'Activity_Date',
                  'ID_Personnel', 'ID_Assignment']


# class DetailActivityForm(ModelForm):
#     class Meta:
#         model = DetailActivity
#         fields = ['ID_ProjectTask', 'ID_Activity',
#                   'Description', 'Location', 'PctTaskComplete']
