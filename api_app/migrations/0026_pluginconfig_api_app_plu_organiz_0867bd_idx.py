# Generated by Django 4.1.7 on 2023-04-14 07:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api_app", "0025_comment"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="pluginconfig",
            index=models.Index(
                fields=[
                    "organization",
                    "owner",
                    "attribute",
                    "type",
                    "plugin_name",
                    "config_type",
                ],
                name="api_app_plu_organiz_0867bd_idx",
            ),
        ),
        migrations.RemoveIndex(
            model_name="pluginconfig",
            name="api_app_plu_type_92301a_idx",
        ),
        migrations.RemoveIndex(
            model_name="pluginconfig",
            name="api_app_plu_organiz_0867bd_idx",
        ),
        migrations.RemoveIndex(
            model_name="pluginconfig",
            name="api_app_plu_owner_i_ff141f_idx",
        ),
    ]
