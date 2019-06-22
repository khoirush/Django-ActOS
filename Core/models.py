from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime, timedelta, date

# Create your models here.


class Personnel (models.Model):
    ID_Personnel = models.IntegerField(primary_key=True, default=0)  # - INT
    First_Name = models.CharField(max_length=20)  # - CHAR 20
    Last_Name = models.CharField(max_length=20)  # - CHAR 20
    Position = models.CharField(max_length=20)  # - CHAR 20)
    Personnel_status = [
        ('E', 'Employee'),
        ('O', 'Outsource'),
        ('C', 'Contract')
    ]
    Status = models.CharField(
        max_length=2,
        choices=Personnel_status,
        default='E'
    )


class Customer(models.Model):
    ID_Customer = models.AutoField(primary_key=True)
    Customer_Name = models.CharField(max_length=50)


class Vendor(models.Model):
    ID_Vendor = models.AutoField(primary_key=True)
    Vendor_Name = models.CharField(max_length=50)


class Project(models.Model):
    ID_Project = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    Description = models.TextField(blank=True)
    # Project_Manager = models.ForeignKey(
    #     to=Personnel, on_delete=models.DO_NOTHING, default=0, null=True)
    Total_Mandays = models.IntegerField(blank=False, default=0)
    Start_Date = models.DateField(blank=False)
    End_Date = models.DateField(blank=False)
    Created_On = models.DateTimeField(auto_now_add=True)
    Last_Update = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.Title)
        super(Project, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('Core:project_index')


class ProjectTask(models.Model):
    ID_Task = models.AutoField(primary_key=True)
    ID_Project = models.ForeignKey(
        'Project', on_delete=models.CASCADE, related_name='project')
    Priority_level = [
        ('H', 'HIGH'),
        ('M', 'MEDIUM'),
        ('L', 'LOW')
    ]
    Priority = models.CharField(
        max_length=10, choices=Priority_level, default='M')
    Title = models.CharField(max_length=255)
    Description = models.TextField(blank=True)
    Task_status = [
        ('OG', 'On-Going'),
        ('DN', 'Done'),
        ('PD', 'Pending')
    ]
    Status = models.CharField(max_length=2, choices=Task_status, default='OG')
    PctComplete = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    PctWeight = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    Start_Date = models.DateField(blank=False)
    TargetFinish_Date = models.DateField(blank=False)
    Target_Duration = models.IntegerField(default=0)
    Created_On = models.DateTimeField(auto_now_add=True)
    Last_Update = models.DateTimeField(auto_now=True)
    # consisting list of ID_Personnel separated by ','
    PIC = models.CharField(max_length=255)
    Total_Mandays = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # subject to Re-Check / Validate Result of Target_Duration
        d1 = date.fromisoformat(str(self.Start_Date))
        d2 = date.fromisoformat(str(self.TargetFinish_Date))
        delta = d2-d1
        self.Target_Duration = delta.days
        self.Total_Mandays = len(
            str.split(self.PIC, ',')) * self.Target_Duration
        super(ProjectTask, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('Core:task_index')


class ProjectAssignment(models.Model):
    ID_Assignment = models.CharField(max_length=10)
    ID_Personnel = models.ForeignKey(
        to='Personnel', on_delete=models.PROTECT)
    ID_Project = models.ForeignKey(
        to='Project', on_delete=models.PROTECT)
    is_PM = models.BooleanField(default=False)
    Start_Date = models.DateField(blank=False)
    End_Date = models.DateField(blank=False)
    Created_On = models.DateTimeField(auto_now_add=True)
    Last_Update = models.DateTimeField(auto_now=True)


class ActivityLog(models.Model):
    ID_Activity = models.AutoField(primary_key=True)
    Activity_Date = models.DateField(blank=False, unique=True)
    ID_Personnel = models.ForeignKey(to='Personnel', on_delete=models.CASCADE)
    ID_Assignment = models.ForeignKey(
        to='ProjectAssignment', on_delete=models.CASCADE)
    ID_ProjectTask = models.ForeignKey(
        to='ProjectTask', on_delete=models.DO_NOTHING)
    Description = models.TextField(blank=True)
    Loc_Options = [
        ('R', 'Remote'),
        ('O', 'Office'),
        ('C', 'Customer Site')
    ]
    Location = models.CharField(max_length=1, choices=Loc_Options, default='O')
    is_Approve = models.BooleanField(default=False)
    Created_On = models.DateTimeField(auto_now_add=True)
    Last_Update = models.DateTimeField(auto_now=True)


# class DetailActivity(models.Model):
#     ID_ProjectTask = models.ForeignKey(
#         to='ProjectTask', on_delete=models.DO_NOTHING)
#     ID_Activity = models.ForeignKey(to='ActivityLog', on_delete=models.CASCADE)
#     Description = models.CharField(max_length=500)
#     Loc_Options = [
#         ('R', 'Remote'),
#         ('O', 'Office'),
#         ('C', 'Customer Site')
#     ]
#     Location = models.CharField(max_length=1, choices=Loc_Options, default='O')
#     PctTaskComplete = models.FloatField(
#         validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
#     Created_On = models.DateTimeField(auto_now_add=True)
#     Last_Update = models.DateTimeField(auto_now=True)


class UserPersonnel(models.Model):
    ID_User = models.OneToOneField(User, on_delete=models.CASCADE)
    ID_Personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE)
