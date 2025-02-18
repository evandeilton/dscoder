from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from dataclasses import dataclass
import os

from openai import OpenAI
from anthropic import Anthropic

@dataclass
class LLMResponse:
    """Class to standardize responses from different LLM providers"""
    content: str
    tokens_used: int
    model: str
    provider: str

class LLMProvider(ABC):
    """Abstract base class for LLM providers"""
    
    @abstractmethod
    def initialize_client(self) -> None:
        pass
    
    @abstractmethod
    def generate_completion(
        self,
        messages: List[Dict[str, str]],
        max_tokens: int,
        temperature: float,
        model: Optional[str] = None
    ) -> LLMResponse:
        pass

class OpenAIProvider(LLMProvider):
    """Provider for OpenAI"""
    
    def __init__(self):
        self.client = None
        self.default_model = "gpt-4"
    
    def initialize_client(self) -> None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        self.client = OpenAI(api_key=api_key)
    
    def generate_completion(
        self,
        messages: List[Dict[str, str]],
        max_tokens: int,
        temperature: float,
        model: Optional[str] = None
    ) -> LLMResponse:
        if not self.client:
            self.initialize_client()
            
        response = self.client.chat.completions.create(
            model=model or self.default_model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature
        )
        
        return LLMResponse(
            content=response.choices[0].message.content,
            tokens_used=response.usage.total_tokens,
            model=model or self.default_model,
            provider="openai"
        )

class AnthropicProvider(LLMProvider):
    """Provider for Anthropic"""
    
    def __init__(self):
        self.client = None
        self.default_model = "claude-3-5-sonnet-20241022"
    
    def initialize_client(self) -> None:
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment variables")
        self.client = Anthropic(api_key=api_key)
    
    def _convert_messages(self, messages: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """Converts messages from OpenAI format to Anthropic format"""
        converted = []
        for msg in messages:
            role = msg["role"]
            content = msg["content"]
            if role == "system":
                converted.append({"role": "assistant", "content": content})
            elif role in ["user", "assistant"]:
                converted.append({"role": role, "content": content})
            else:
                logging.warning(f"Unsupported message type: {role}")
        return converted
    
    def generate_completion(
        self,
        messages: List[Dict[str, str]],
        max_tokens: int,
        temperature: float,
        model: Optional[str] = None
    ) -> LLMResponse:
        if not self.client:
            self.initialize_client()
            
        anthropic_messages = self._convert_messages(messages)
        
        response = self.client.messages.create(
            model=model or self.default_model,
            messages=anthropic_messages,
            max_tokens=max_tokens,
            temperature=temperature
        )
        
        return LLMResponse(
            content=response.content[0].text,
            tokens_used=response.usage.output_tokens + response.usage.input_tokens,
            model=model or self.default_model,
            provider="anthropic"
        )

class DeepSeekProvider(LLMProvider):
    """
    Provider for the DeepSeek API that uses the same interface as OpenAI.
    
    Attributes:
        client: OpenAI client configured for the DeepSeek API
        default_model: Default DeepSeek model to use
        base_url: Base URL of the DeepSeek API
    """
    
    def __init__(self):
        self.client = None
        self.default_model = "deepseek-chat"
        self.base_url = "https://api.deepseek.com"
    
    def initialize_client(self) -> None:
        """
        Initializes the OpenAI client with DeepSeek configurations.
        
        Raises:
            ValueError: If DEEPSEEK_API_KEY is not set in environment variables
        """
        api_key = os.getenv("DEEPSEEK_API_KEY")
        if not api_key:
            raise ValueError("DEEPSEEK_API_KEY not found in environment variables")
            
        self.client = OpenAI(
            api_key=api_key,
            base_url=self.base_url
        )
    
    def generate_completion(
        self,
        messages: List[Dict[str, str]],
        max_tokens: int,
        temperature: float,
        model: Optional[str] = None
    ) -> LLMResponse:
        """
        Generates a completion using the DeepSeek API.
        
        Args:
            messages: List of messages in OpenAI format
            max_tokens: Maximum number of tokens in the response
            temperature: Generation temperature (creativity)
            model: Specific model to use (optional)
            
        Returns:
            LLMResponse: Standardized response containing generated content and metadata
            
        Raises:
            RuntimeError: If the client is not initialized
        """
        if not self.client:
            self.initialize_client()
            
        response = self.client.chat.completions.create(
            model=model or self.default_model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature
        )
        
        return LLMResponse(
            content=response.choices[0].message.content,
            tokens_used=response.usage.total_tokens,
            model=model or self.default_model,
            provider="deepseek"
        )

class OpenRouterProvider(LLMProvider):
    """Provider for OpenRouter API that provides access to multiple LLM models"""
    
    def __init__(self):
        self.client = None
        self.default_model = "google/gemini-2.0-pro-exp-02-05:free"  # Default model
        self.base_url = "https://openrouter.ai/api/v1"
    
    def initialize_client(self) -> None:
        """
        Initializes the OpenAI client with OpenRouter configurations
        
        Raises:
            ValueError: If OPENROUTER_API_KEY is not set in environment variables
        """
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            raise ValueError("OPENROUTER_API_KEY not found in environment variables")
            
        self.client = OpenAI(
            api_key=api_key,
            base_url=self.base_url,
            default_headers={
                "HTTP-Referer": "https://github.com/evandeilton/dscoder",  # Update with your repo
                "X-Title": "DSCoder"
            }
        )
    
    def generate_completion(
        self,
        messages: List[Dict[str, str]],
        max_tokens: int,
        temperature: float,
        model: Optional[str] = None
    ) -> LLMResponse:
        """
        Generates a completion using the OpenRouter API
        
        Args:
            messages: List of messages in OpenAI format
            max_tokens: Maximum tokens in response
            temperature: Generation temperature
            model: Specific model to use (optional)
            
        Returns:
            LLMResponse: Standardized response with content and metadata
        """
        if not self.client:
            self.initialize_client()
            
        try:
            response = self.client.chat.completions.create(
                model=model or self.default_model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature
            )
            
            return LLMResponse(
                content=response.choices[0].message.content,
                tokens_used=response.usage.total_tokens,
                model=model or self.default_model,
                provider="openrouter"
            )
        except Exception as e:
            logging.error(f"OpenRouter API error: {str(e)}")
            raise