from {{ cookiecutter.package_name }}.kitchen import app as kitchen
from kitchenai.contrib.kitchenai_sdk.api import EmbedSchema
import logging

logger = logging.getLogger(__name__)


@kitchen.query("query")
async def query(text: EmbedSchema, metadata: dict = {}, **kwargs):
    """
    Example: 
    @kitchen.query("query")
    async def query(data: QuerySchema):
        chroma_collection = chroma_client.get_or_create_collection("quickstart")


        vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

        index = VectorStoreIndex.from_vector_store(
            vector_store,
        )

        query_engine = index.as_query_engine(chat_mode="best", llm=llm, verbose=True)
        response = await query_engine.aquery(data.query)

        return {"msg": response.response}
    """
    pass




