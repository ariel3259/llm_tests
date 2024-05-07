from strategies import LLMStrategy, EmbeddingsStrategy
from langchain.chat_models.vertexai import ChatVertexAI

class GeminiLLMStrategy(LLMStrategy):
    def __init__(self, model, token):
        super().__init__(model, token)
    
    def get_model(self):
