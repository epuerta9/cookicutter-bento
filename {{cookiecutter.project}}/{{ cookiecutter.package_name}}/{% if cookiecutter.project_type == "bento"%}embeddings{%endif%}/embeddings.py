from {{ cookiecutter.package_name }}.kitchen import app as kitchen
from kitchenai.contrib.kitchenai_sdk.api import EmbedSchema
import logging

logger = logging.getLogger(__name__)


@kitchen.embed("{{cookiecutter.project}}")
async def embeddings(text: EmbedSchema, metadata: dict = {}, **kwargs):
    pass




