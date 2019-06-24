from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.


class PersonnelAdmin(admin.ModelAdmin):
    list_display = ('ID_Personnel', 'First_Name',
                    'Last_Name', 'Position', 'Status')
    list_display_links = ('ID_Personnel', 'First_Name',
                          'Last_Name', 'Position', 'Status')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('ID_Customer', 'Customer_Name')
    list_display_links = ('ID_Customer', 'Customer_Name')


class VendorAdmin(admin.ModelAdmin):
    list_display = ('ID_Vendor', 'Vendor_Name')
    list_display_links = ('ID_Vendor', 'Vendor_Name')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('ID_Project', 'Title', 'Start_Date', 'End_Date')
    list_display_links = ('ID_Project', 'Title', 'Start_Date', 'End_Date')


class ProjectTaskAdmin(admin.ModelAdmin):
    list_display = ('ID_Task', 'ID_Project', 'Priority',
                    'Title', 'PIC', 'Start_Date', 'TargetFinish_Date')
    list_display_links = ('ID_Task', 'ID_Project', 'Priority',
                          'Title', 'PIC', 'Start_Date', 'TargetFinish_Date')


class ProjectAssignmentAdmin(admin.ModelAdmin):
    list_display = ('ID_Personnel',
                    'ID_Project', 'Start_Date', 'End_Date')
    list_display_links = ( 'ID_Personnel',
                          'ID_Project', 'Start_Date', 'End_Date')


class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('ID_Activity', 'Activity_Date',
                    'ID_Personnel', 'ID_Assignment')
    list_display_links = ('ID_Activity', 'Activity_Date',
                          'ID_Personnel', 'ID_Assignment')


# class DetailActivityAdmin(admin.ModelAdmin):
#     list_display = ('ID_ProjectTask', 'ID_Activity', 'Description')
#     list_display_links = ('ID_ProjectTask', 'ID_Activity', 'Description')


class UserPersonnelAdmin(admin.ModelAdmin):
    list_display = ('ID_User', 'ID_Personnel')
    list_display_links = ('ID_User', 'ID_Personnel')


admin.site.register(Personnel, PersonnelAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectTask, ProjectTaskAdmin)
admin.site.register(ProjectAssignment, ProjectAssignmentAdmin)
admin.site.register(ActivityLog, ActivityLogAdmin)
# admin.site.register(DetailActivity, DetailActivityAdmin)
admin.site.register(UserPersonnel, UserPersonnelAdmin)
