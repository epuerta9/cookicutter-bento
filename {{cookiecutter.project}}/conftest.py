import os
import django
from django.conf import settings

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kitchenai_cookbook.tests.settings')
django.setup()

# Only import other Django-related items after setup
import pytest
from django.apps import apps

@pytest.fixture
def kitchen_app():
    """Fixture to provide the KitchenAI app instance"""
    kitchenai_config = apps.get_app_config("kitchenai_cookbook")
    return kitchenai_config.kitchenai_app

@pytest.fixture
def api_client():
    """Fixture for API testing"""
    from django.test.client import Client
    return Client() 