from django.apps import AppConfig


class {{ cookiecutter.package_name.upper() | replace('_', ' ') | replace('-', ' ') | title | replace(' ', '') }}Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "{{ cookiecutter.package_name }}"

    def ready(self):
        """Initialize KitchenAI app when Django starts"""
        {% if cookiecutter.project_type == "bento" %}
        import {{ cookiecutter.package_name }}.storage.vector
        import {{ cookiecutter.package_name }}.query.query
        import {{ cookiecutter.package_name }}.embeddings.embeddings
        {% else %}
        pass
        {% endif %}
