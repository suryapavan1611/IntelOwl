# This file is a part of IntelOwl https://github.com/intelowlproject/IntelOwl
# See the file 'LICENSE' for copying permission.

# Generated by Django 3.2.18 on 2023-03-07 08:29

from django.db import migrations


def migrate(apps, schema_editor):
    ...


def reverse_migrate(apps, schema_editor):
    ConnectorReport = apps.get_model("connectors_manager", "ConnectorReport")
    for report in ConnectorReport.objects.all():
        report.parent_playbook = report.job.playbook_to_execute
        report.save()

class Migration(migrations.Migration):

    dependencies = [
        ('connectors_manager', '0009_parent_playbook_foreign_key'),
        ('api_app', '0022_single_playbook_post_migration'),
    ]

    operations = [
        migrations.RunPython(
            migrate, reverse_migrate
        ),
        migrations.RemoveField(
            model_name='connectorreport',
            name="parent_playbook",
        )

    ]
