from django.apps import AppConfig


class BentoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "{{ cookiecutter.package_name}}_bento"