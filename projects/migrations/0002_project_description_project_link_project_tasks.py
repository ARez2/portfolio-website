# Generated by Django 4.2.5 on 2023-09-09 16:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="description",
            field=models.TextField(default="", verbose_name="Project description"),
        ),
        migrations.AddField(
            model_name="project",
            name="link",
            field=models.CharField(default="", max_length=200),
        ),
        migrations.AddField(
            model_name="project",
            name="tasks",
            field=models.TextField(
                default="", verbose_name="Challenges of that project"
            ),
        ),
    ]
