# Generated by Django 5.0.4 on 2024-05-09 20:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("applicants", "0002_rename_student_application_applicant"),
    ]

    operations = [
        migrations.AddField(
            model_name="application",
            name="answers_to_ques",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="application",
            name="stage",
            field=models.IntegerField(default=1),
        ),
    ]