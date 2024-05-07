from abc import ABCMeta, abstractmethod

class LLMStrategy(metaclass=ABCMeta):
    def __init__(self, model, token):
        self.model = model
        self.token = token

    @abstractmethod
    def get_model(self):
        pass

class EmbeddingsStrategy(metaclass=ABCMeta):
    def __init__(self, model, token):
        self.model = model
        self.token = token
    
    @abstractmethod
    def get_embedding(self):
        pass