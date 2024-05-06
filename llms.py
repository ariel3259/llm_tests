#from langchain_community
from langchain_openai import ChatOpenAI
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.llms.huggingface_hub import HuggingFaceHub
from langchain.chat_models.vertexai import ChatVertexAI
from langchain.embeddings.vertexai import VertexAIEmbeddings
from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings

class LLMType():
    #type = openai | sentence-transformer | geminis
    def __init__(self, type, model, token):
        self.type = type
        self.model = model
        self.token = token
    

class EmbeddingType():
    #type =  openai | sentence-transformer | geminis
    def __init__(self, type, embedding):
        self.type = type
        self.embedding = embedding