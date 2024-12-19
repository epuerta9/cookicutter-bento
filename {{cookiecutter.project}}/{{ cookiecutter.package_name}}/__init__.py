from django.urls import path
from django.conf import settings
import djp
from llama_index.llms.openai import OpenAI


llm = OpenAI(model="gpt-4")

@djp.hookimpl
def installed_apps():
    return ["{{ cookiecutter.package_name }}"]


@djp.hookimpl
def urlpatterns():
    # A list of URL patterns to add to urlpatterns:
    return []


@djp.hookimpl
def settings(current_settings):
    # Make changes to the Django settings.py globals here
    current_settings["KITCHENAI"]["{{ cookiecutter.project_type }}"].append({
        "name": "{{ cookiecutter.package_name }}",
        "description": "{{ cookiecutter.project_description }}",
        "tags": ["{{ cookiecutter.project_suffix }}", "{{ cookiecutter.project_type }}", "{{cookiecutter.package_name}}", "{{cookiecutter.project}}"],
    })
    


@djp.hookimpl
def middleware():
    # A list of middleware class strings to add to MIDDLEWARE:
    # Wrap strings in djp.Before("middleware_class_name") or
    # djp.After("middleware_class_name") to specify before or after
    return []