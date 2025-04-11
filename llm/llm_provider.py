# llm/llm_provider.py
from abc import ABC, abstractmethod

class LLMProvider(ABC):
    @abstractmethod
    def ask(self, prompt:str) -> str:
        pass
    