# Generated by Django 5.0 on 2024-01-30 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('day4app', '0002_alter_course_course_credit'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_type',
            field=models.CharField(choices=[('THEORY', 'Theory Course'), ('LAB', 'Lab Course'), ('PROJECT', 'Project Course')], default='THEORY', max_length=10),
        ),
    ]