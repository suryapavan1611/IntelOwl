# Generated by Django 4.1.9 on 2023-06-14 13:05

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("visualizers_manager", "0023_alter_visualizerconfig_name"),
        ("certego_saas_organization", "0001_initial"),
        ("api_app", "0033_alter_parameter_unique_together"),
        ("analyzers_manager", "0031_alter_analyzerconfig_name"),
        ("connectors_manager", "0018_alter_connectorconfig_name"),
        ("playbooks_manager", "0016_playbookconfig_disabled_in_organizations"),
    ]

    operations = [
        migrations.CreateModel(
            name="PivotConfig",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField()),
                ("disabled", models.BooleanField(default=False)),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^\\w+(\\.\\w+)*$",
                                message="Object should be a python path",
                            )
                        ],
                    ),
                ),
                (
                    "field",
                    models.CharField(
                        help_text="Dotted path to the field",
                        max_length=256,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^\\w+(\\.\\w+)*$",
                                message="Object should be a python path",
                            )
                        ],
                    ),
                ),
                (
                    "analyzer_config",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="pivots",
                        to="analyzers_manager.analyzerconfig",
                    ),
                ),
                (
                    "connector_config",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="pivots",
                        to="connectors_manager.connectorconfig",
                    ),
                ),
                (
                    "disabled_in_organizations",
                    models.ManyToManyField(
                        blank=True,
                        related_name="%(app_label)s_%(class)s_disabled",
                        to="certego_saas_organization.organization",
                    ),
                ),
                (
                    "playbook_to_execute",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="executed_by_pivot",
                        to="playbooks_manager.playbookconfig",
                    ),
                ),
                (
                    "visualizer_config",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="pivots",
                        to="visualizers_manager.visualizerconfig",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Pivot",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "ending_job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pivot_parents",
                        to="api_app.job",
                    ),
                ),
                (
                    "pivot_config",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="pivots_manager.pivotconfig",
                    ),
                ),
                (
                    "starting_job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pivot_children",
                        to="api_app.job",
                    ),
                ),
            ],
        ),
        migrations.AddIndex(
            model_name="pivotconfig",
            index=models.Index(
                fields=["analyzer_config"], name="pivot_manag_analyze_4e863b_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="pivotconfig",
            index=models.Index(
                fields=["connector_config"], name="pivot_manag_connect_2afb9a_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="pivotconfig",
            index=models.Index(
                fields=["visualizer_config"], name="pivot_manag_visuali_44b587_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="pivotconfig",
            index=models.Index(
                fields=["playbook_to_execute"], name="pivot_manag_playboo_119fe0_idx"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="pivotconfig",
            unique_together={
                ("analyzer_config", "field", "playbook_to_execute"),
                ("connector_config", "field", "playbook_to_execute"),
                ("visualizer_config", "field", "playbook_to_execute"),
            },
        ),
        migrations.AddIndex(
            model_name="pivot",
            index=models.Index(
                fields=["starting_job"], name="pivot_manag_startin_21e74a_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="pivot",
            index=models.Index(
                fields=["pivot_config"], name="pivot_manag_pivot_c_e1027b_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="pivot",
            index=models.Index(
                fields=["ending_job"], name="pivot_manag_ending__6d1c06_idx"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="pivot",
            unique_together={("starting_job", "pivot_config", "ending_job")},
        ),
    ]
