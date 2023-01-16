# Generated by Django 4.0.5 on 2023-01-09 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='department_name',
            new_name='Department_name',
        ),
        migrations.RenameField(
            model_name='department',
            old_name='description',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='department',
            old_name='status',
            new_name='Status',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='doj',
            new_name='DOJ',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='department',
            new_name='Department',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='designation',
            new_name='Designation',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='empname',
            new_name='Empname',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='contact',
        ),
        migrations.AddField(
            model_name='employees',
            name='Contact',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='employees',
            name='Salary',
            field=models.CharField(max_length=50, null=True),
        ),
    ]