# Generated by Django 3.0.7 on 2024-03-21 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0006_alter_customuser_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
    ]
