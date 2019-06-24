# Generated by Django 2.2.2 on 2019-06-23 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0007_auto_20190619_0746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectassignment',
            name='ID_Assignment',
        ),
        migrations.AlterField(
            model_name='activitylog',
            name='ID_Assignment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignment', to='Core.ProjectAssignment'),
        ),
        migrations.AlterField(
            model_name='projectassignment',
            name='ID_Personnel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='assigned_project', to='Core.Personnel'),
        ),
        migrations.AlterField(
            model_name='projectassignment',
            name='ID_Project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='assigned_team', to='Core.Project'),
        ),
        migrations.AlterField(
            model_name='projecttask',
            name='ID_Project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task', to='Core.Project'),
        ),
    ]