# Generated by Django 4.2.11 on 2024-04-04 07:46

from django.conf import settings
from django.db import migrations


def migrate(apps, schema_editor):
    User = apps.get_model(*settings.AUTH_USER_MODEL.split("."))
    Profile = apps.get_model("authentication", "UserProfile")
    for user in User.objects.all():
        is_robot = user.username.endswith("Ingestor")
        if not hasattr(user, "profile") or not user.profile:
            profile = Profile(
                user=user, task_priority=7 if is_robot else 10, is_robot=is_robot
            )
        else:
            profile = user.profile
            profile.task_priority=7 if is_robot else 10
            profile.is_robot=is_robot
        profile.save()


def reverse_migrate(apps, schema_editor):
    Profile = apps.get_model("authentication", "UserProfile")
    Profile.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("authentication", "0004_alter_userprofile_company_name_and_more"),
    ]

    operations = [migrations.RunPython(migrate, reverse_migrate)]
