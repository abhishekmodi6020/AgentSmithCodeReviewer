# llm/openai_client.py
"""
Functions to interact with OpenAI’s API — sending code for review
"""
import openai
import os
from llm.llm_provider import LLMProvider

class OpenAIClient(LLMProvider):
    """
    Temperature controls the creativity vs consistency of the LLM output.
    max_toxens defines the maximum length of the response (output) the LLM can generate.
    """    
     

    def __init__(self, model: str = "gpt-3.5-turbo", temperature: float = 0.7, max_tokens: int = 1000):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def ask(self, prompt: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a code review assistant specialized in SOLID principles and design pattern recommendations."},
                    {"role": "user", "content": prompt}
                ],
                temperature=self.temperature,
                max_tokens=self.max_tokens,
            )
            first_choice = response['choices'][0]
            message = first_choice['message']
            llm_reply = message['content']
            return llm_reply
        except Exception as e:
            print(f"❌ Error in LLM response: {e}")
            return "Error: Could not generate a response from the language model."
