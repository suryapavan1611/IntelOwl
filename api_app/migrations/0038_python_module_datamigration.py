# Generated by Django 4.1.10 on 2023-08-22 12:36
from django.core.exceptions import ValidationError
from django.db import migrations


def migrate(apps, schema_editor):
    PythonModule = apps.get_model("api_app", "PythonModule")
    Parameter = apps.get_model("api_app", "Parameter")
    AnalyzerConfig = apps.get_model("analyzers_manager", "AnalyzerConfig")
    ConnectorConfig = apps.get_model("connectors_manager", "ConnectorConfig")
    VisualizerConfig = apps.get_model("visualizers_manager", "VisualizerConfig")
    IngestorConfig = apps.get_model("ingestors_manager", "IngestorConfig")
    for config in AnalyzerConfig.objects.all():
        if config.type == "file" and not config.run_hash:
            module = PythonModule.objects.get_or_create(
                module=config.python_module,
                base_path="api_app.analyzers_manager.file_analyzers",
            )[0]
            if "android" in config.supported_filetypes:
                config.supported_filetypes.remove("android")
                config.supported_filetypes.append(
                    "application/vnd.android.package-archive"
                )
        else:
            module = PythonModule.objects.get_or_create(
                module=config.python_module,
                base_path="api_app.analyzers_manager.observable_analyzers",
            )[0]
        config.python_module2 = module
        config.full_clean()
        config.save()
    for config in ConnectorConfig.objects.all():
        module = PythonModule.objects.get_or_create(
            module=config.python_module,
            base_path="api_app.connectors_manager.connectors",
        )[0]
        config.python_module2 = module
        config.full_clean()
        config.save()
    for config in VisualizerConfig.objects.all():
        module = PythonModule.objects.get_or_create(
            module=config.python_module,
            base_path="api_app.visualizers_manager.visualizers",
        )[0]
        config.python_module2 = module
        config.full_clean()
        config.save()
    for config in IngestorConfig.objects.all():
        module = PythonModule.objects.get_or_create(
            module=config.python_module, base_path="api_app.ingestors_manager.ingestors"
        )[0]
        config.python_module2 = module
        config.full_clean()
        config.save()
    saved_params = {}

    for param in Parameter.objects.all():
        config = (
            param.analyzer_config
            or param.connector_config
            or param.visualizer_config
            or param.ingestor_config
        )
        for plugin_config in param.values.all():
            plugin_config.analyzer_config = param.analyzer_config
            plugin_config.connector_config = param.connector_config
            plugin_config.visualizer_config = param.visualizer_config
            plugin_config.visualizer_config = param.visualizer_config
            plugin_config.ingestor_config = param.ingestor_config
            plugin_config.full_clean()
            plugin_config.save()
        param.python_module = config.python_module2
        try:
            param.full_clean()
        except ValidationError:
            for plugin_config in param.values.all():
                plugin_config.analyzer_config = param.analyzer_config
                plugin_config.connector_config = param.connector_config
                plugin_config.visualizer_config = param.visualizer_config
                plugin_config.visualizer_config = param.visualizer_config
                plugin_config.ingestor_config = param.ingestor_config
                plugin_config.parameter = saved_params[
                    (param.name, param.python_module)
                ]
                try:
                    plugin_config.full_clean()
                except ValidationError:
                    plugin_config.delete()
                else:
                    plugin_config.save()
            param.delete()
        else:
            for plugin_config in param.values.all():
                plugin_config.analyzer_config = param.analyzer_config
                plugin_config.connector_config = param.connector_config
                plugin_config.visualizer_config = param.visualizer_config
                plugin_config.visualizer_config = param.visualizer_config
                plugin_config.ingestor_config = param.ingestor_config
                try:
                    plugin_config.full_clean()
                except ValidationError:
                    plugin_config.delete()
                else:
                    plugin_config.save()
                plugin_config.save()
            param.save()
            saved_params[(param.name, param.python_module)] = param


class Migration(migrations.Migration):
    dependencies = [
        (
            "connectors_manager",
            "0019_rename_connectors__python__0fb146_idx_connectors__python__f23fd8_idx_and_more",
        ),
        (
            "visualizers_manager",
            "0024_rename_visualizers_python__2c4ded_idx_visualizers_python__8b1832_idx_and_more",
        ),
        (
            "ingestors_manager",
            "0005_rename_ingestors_m_python__5c8ce0_idx_ingestors_m_python__b7a859_idx_and_more",
        ),
        ("analyzers_manager", "0039_alter_analyzerconfig_python_module"),
        ("api_app", "0037_pythonmodule_and_more"),
    ]

    operations = [
        migrations.RunPython(migrate),
    ]
