# This file is a part of IntelOwl https://github.com/intelowlproject/IntelOwl
# See the file 'LICENSE' for copying permission.

# Generated by Django 3.2.16 on 2023-01-23 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api_app", "0012_auto_20221227_1543"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="observable_classification",
            field=models.CharField(
                blank=True,
                choices=[
                    ("ip", "Ip"),
                    ("url", "Url"),
                    ("domain", "Domain"),
                    ("hash", "Hash"),
                    ("generic", "Generic"),
                    ("", "Empty"),
                ],
                max_length=12,
            ),
        ),
    ]
