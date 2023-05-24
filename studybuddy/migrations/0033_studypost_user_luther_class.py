# Generated by Django 4.1.1 on 2022-11-09 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("studybuddy", "0032_alter_studypost_user_class"),
    ]

    operations = [
        migrations.AddField(
            model_name="studypost",
            name="user_luther_class",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_luther_class",
                to="studybuddy.lutherclass",
            ),
        ),
    ]