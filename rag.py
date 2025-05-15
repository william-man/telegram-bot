from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding


class Rag:
    def __init__(self):
        self.llm = Ollama(model="llama3.2", request_timeout=120.0)
        self.embed_model = OllamaEmbedding(model_name="nomic-embed-text")

        Settings.llm = self.llm
        Settings.embed_model = self.embed_model

        documents = SimpleDirectoryReader("data").load_data()
        index = VectorStoreIndex.from_documents(documents)
        self.query_engine = index.as_query_engine()
    
    def query(self, query: str)->None:
        response = self.query_engine.query(query)
        return response

    def direct(self, prompt: str) -> None:
        response = self.llm.complete(prompt)
        print(response.text)

