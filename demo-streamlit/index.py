from llama_index import download_loader, VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.tools import QueryEngineTool, ToolMetadata
from llama_index.query_engine import SubQuestionQueryEngine
from llama_index.callbacks import CallbackManager, LlamaDebugHandler
from llama_index.llms import LlamaCPP

from utils import completion_to_prompt, messages_to_prompt


def build_service_context():
    return ServiceContext.from_defaults(llm=LlamaCPP(
        model_path=None,
        messages_to_prompt=messages_to_prompt,
        completion_to_prompt=completion_to_prompt,
        model_kwargs={"n_gpu_layers": 50},
    ))

def build_index(documents, context):
    index = VectorStoreIndex.from_documents(documents, service_context=context)
    return index


