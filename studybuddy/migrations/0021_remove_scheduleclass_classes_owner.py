# Generated by Django 4.1.1 on 2022-11-05 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("studybuddy", "0020_scheduleclass_classes_owner"),
    ]

    operations = [
        migrations.RemoveField(model_name="scheduleclass", name="classes_owner",),
    ]
