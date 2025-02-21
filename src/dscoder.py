# File system and environment
import os
import subprocess
import logging
from pathlib import Path
from datetime import datetime
import re
import tempfile
import shutil

# Arguments and environment
from argparse import ArgumentParser
from dotenv import load_dotenv

# Types
from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass

# UI
from rich.console import Console
from rich.table import Table
from rich.logging import RichHandler

# LLM APIs
from openai import OpenAI
from anthropic import Anthropic

from llm_providers import (
    LLMProvider, OpenAIProvider, AnthropicProvider, 
    DeepSeekProvider, OpenRouterProvider, LLMResponse
)

class ErrorHandler:
    """System error handler"""
    
    def __init__(self):
        self.console = Console()
        
    def handle_error(self, error: Exception, context: str = "") -> str:
        """
        Processes and formats system errors
        
        Args:
            error: Caught exception
            context: Additional error context
            
        Returns:
            str: Formatted error message
        """
        error_msg = f"{type(error).__name__}: {str(error)}"
        if context:
            error_msg = f"{context}: {error_msg}"
        return error_msg

class MetricsCollector:
    """Execution metrics collector"""
    
    def __init__(self):
        self.total_tokens = 0
        self.successful_generations = 0
        self.failed_generations = 0
        self.errors = []
        
    def update_metrics(self, tokens: int, success: bool, error: str = None):
        """Updates execution metrics"""
        self.total_tokens += tokens
        if success:
            self.successful_generations += 1
        else:
            self.failed_generations += 1
            if error:
                self.errors.append(error)
    
    def display_metrics(self, console: Console):
        """Displays metrics in a formatted table"""
        table = Table(title="Execution Metrics")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="magenta")
        
        table.add_row("Total Tokens", str(self.total_tokens))
        table.add_row("Successful Generations", str(self.successful_generations))
        table.add_row("Failed Generations", str(self.failed_generations))
        table.add_row("Total Errors", str(len(self.errors)))
        
        console.print(table)

class LLMClient:
    """Generic client for LLMs that manages different providers"""
    
    def __init__(self, provider: str = "openrouter"):
        load_dotenv()
        self.providers = {
            "openai": OpenAIProvider(),
            "anthropic": AnthropicProvider(),
            "deepseek": DeepSeekProvider(),
            "openrouter": OpenRouterProvider()  # Add OpenRouter provider
        }
        
        if provider not in self.providers:
            raise ValueError(f"Provider {provider} not supported. Available providers: {', '.join(self.providers.keys())}")
            
        self.current_provider = self.providers[provider]
        self.current_provider.initialize_client()
    
    def switch_provider(self, provider: str) -> None:
        if provider not in self.providers:
            raise ValueError(f"Provider {provider} not supported")
        self.current_provider = self.providers[provider]
        self.current_provider.initialize_client()
    
    def generate_completion(
        self,
        messages: List[Dict[str, str]],
        max_tokens: int = 5000,
        temperature: float = 0,
        model: Optional[str] = None
    ) -> LLMResponse:
        return self.current_provider.generate_completion(
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
            model=model
        )

class AIAgent:
    def __init__(self, provider: str = "openai", trace: bool = False):
        """Initializes the AI agent"""
        self.llm_client = LLMClient(provider)
        self.trace = trace
        self.console = Console()
        self.error_handler = ErrorHandler()
        self.metrics_collector = MetricsCollector()
        
        # Directory configuration
        self.base_dir = Path("output")
        self.temp_dir = self.base_dir / "temp"
        self.logs_dir = self.base_dir / "logs"
        
        for dir_path in [self.base_dir, self.temp_dir, self.logs_dir]:
            dir_path.mkdir(parents=True, exist_ok=True)
        
        # Logging configuration
        log_format = "%(asctime)s [%(levelname)s] %(message)s"
        log_file = self.logs_dir / f"ai_agent_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        
        logging.basicConfig(
            level=logging.INFO,
            format=log_format,
            handlers=[
                logging.FileHandler(log_file, encoding='utf-8'),
                RichHandler(rich_tracebacks=True)
            ]
        )
        self.logger = logging.getLogger(__name__)
        
        # Message initialization
        self.messages = [
            {
                "role": "system",
                "content": (
                    "You are a senior software engineering assistant specialized in generating high-quality code "
                    "for Python, C++, R, Rcpp, and Julia. Your core requirements are:\n\n"
                    
                    "1. MANDATORY REQUIREMENTS FOR ALL LANGUAGES:\n"
                    "- ALWAYS deliver code in a single, complete, functional block\n"
                    "- ALL helper functions/methods MUST be implemented in the same block\n"
                    "- Code MUST be self-contained with NO external dependencies\n"
                    "- EVERY function used MUST have its complete implementation\n"
                    "- Use ``` markers at the beginning and end of code blocks\n\n"
                    "- Install missing/dependent libraries"
                    
                    "2. LANGUAGE-SPECIFIC REQUIREMENTS:\n"
                    "C++:\n"
                    "- Use ONLY Standard Library (STL) native features\n"
                    "- NO external libraries beyond STL\n"
                    "- Implement all functionality using only native features\n"
                    "- Use modern C++ (17/20) best practices\n\n"
                    
                    "Python:\n"
                    "- Prefer standard and data science libraries\n"
                    "- Include all necessary helper functions\n"
                    "- Use type hints and proper documentation\n\n"
                    
                    "R/Rcpp:\n"
                    "- Include all required helper functions\n"
                    "- Declare all dependencies\n"
                    "- Rcpp code must be pre-compiled by using Rcpp resources\n"
                    "- Ensure self-contained implementation\n\n"
                    
                    "Julia:\n"
                    "- Implement all necessary functions\n"
                    "- Prefer standard and data science packages\n"
                    "- Include all type and method definitions\n"
                    "- Ensure code independence\n\n"
                    
                    "3. IMPLEMENTATION STRUCTURE:\n"
                    "- ALL helper functions must be implemented, even trivial ones\n"
                    "- Include all necessary data structures\n"
                    "- Ensure NO external dependencies\n"
                    "- Maintain logical code organization\n\n"
                    
                    "4. DEVELOPMENT PROCESS:\n"
                    "1. Analyze requirements including mathematics, data science and programming good practices\n"
                    "2. Identify ALL needed functions and methods required\n"
                    "3. Implement EVERYTHING in one block\n"
                    "4. Validate completeness\n\n"
                    
                    "IMPORTANT: Generated code MUST be completely functional without external implementations. "
                    "ALL mentioned or used functions MUST be fully implemented in the same code block. "
                    "For C++, use EXCLUSIVELY STL native resources."
                )
            }
        ]
    
    def log(self, message: str, level: str = "info", force: bool = False):
        """Logs messages"""
        if self.trace or force:
            if level == "error":
                self.logger.error(message)
            elif level == "warning":
                self.logger.warning(message)
            else:
                self.logger.info(message)    

    def extract_code(self, content: str) -> Optional[str]:
        """
        Extracts code from LLM response, supporting multiple languages (R, Python, Julia, C++/Rcpp)
        with content validation.
        
        Args:
            content (str): Complete LLM response content
            
        Returns:
            Optional[str]: Extracted code or None if no valid code found
        """
        # Supported languages and their patterns
        language_patterns: Dict[str, List[str]] = {
            'r': [r'library\(', r'function\(', r'<-', r'%>%'],
            'python': [r'import\s+\w+', r'def\s+\w+\(', r'class\s+\w+:'],
            'julia': [r'using\s+\w+', r'function\s+\w+\(', r'struct\s+\w+'],
            'cpp': [r'#include', r'void\s+\w+\(', r'int\s+\w+\(', r'class\s+\w+\s*\{'],
            'rcpp': [r'//\[\[Rcpp::export\]\]', r'NumericVector', r'DataFrame']
        }
        
        # Common phrases that are not code
        common_phrases = [
            'i will create', 'i will provide', 'here is', 'here\'s', 
            'example', 'we can', 'you can', 'now'
        ]
        
        def detect_language(code: str) -> Optional[str]:
            """Detects code language based on specific patterns."""
            code = code.lower()
            for lang, patterns in language_patterns.items():
                if any(re.search(pattern, code, re.IGNORECASE) for pattern in patterns):
                    return lang
            return None
        
        def validate_code_block(code: str) -> bool:
            """Validates if the extracted block is actually code."""
            # Remove whitespace
            code = code.strip()
            
            # Checks if block is empty
            if not code:
                return False
                
            # Checks for common phrases that are not code
            if any(code.lower().startswith(phrase) for phrase in common_phrases):
                return False
            
            # Checks for common code characters
            code_indicators = ['(', ')', '{', '}', '=', ':', ';', '#', '"', "'"]
            if not any(indicator in code for indicator in code_indicators):
                return False
            
            # Checks if it looks like code from a supported language
            return detect_language(code) is not None
        
        # Searches for markdown code blocks with language specification
        matches = re.finditer(r'```(\w*)\n(.*?)```', content, re.DOTALL)
        
        # List to store valid blocks
        valid_blocks = []
        
        # Processes each found match
        for match in matches:
            lang, code = match.groups()
            code = code.strip()
            
            # If language was specified in markdown, checks if it's supported
            if lang and lang.lower() not in language_patterns:
                continue
            
            # Validates code block
            if validate_code_block(code):
                valid_blocks.append(code)
        
        # Returns first valid block found or None
        return valid_blocks[0] if valid_blocks else None
    
    def save_final_version(self, code: str, language: str, status: str) -> str:
        """Saves final version of generated code"""
        extensions = {
            "python": ".py",
            "cpp": ".cpp",
            "r": ".R",
            "julia": ".jl",
            "rcpp": ".cpp"
        }
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        ext = extensions.get(language.lower(), ".txt")
        filename = f"code_{status}_{timestamp}{ext}"
        
        if status == "temp":
            filepath = self.temp_dir / filename
        else:
            filepath = self.base_dir / filename
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(code)
        
        return str(filepath)
    
    def execute_code(self, file_path: str, language: str) -> Tuple[str, Optional[str]]:
        """Executes generated code"""
        commands = {
            "python": ["python", file_path],
            "cpp": ["g++", file_path, "-o", file_path + ".exe"],
            "r": ["Rscript", file_path],
            "julia": ["julia", file_path],
            "rcpp": ["R", "CMD", "SHLIB", file_path]
        }
        
        if language.lower() not in commands:
            return "", f"Unsupported language: {language}"
        
        try:
            process = subprocess.Popen(
                commands[language.lower()],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            stdout, stderr = process.communicate(timeout=30)
            
            if process.returncode != 0:
                return "", stderr
            
            return stdout, None
            
        except subprocess.TimeoutExpired:
            return "", "Code execution timeout"
        except Exception as e:
            return "", str(e)
    
    def generate_code(
        self,
        description: str,
        language: str = "python",
        expected_output: Optional[str] = None,
        max_attempts: int = 5
    ) -> Optional[str]:
        """Generates code based on provided description"""
        attempts = 0
        previous_code = ""
        error_result = ""
        generated_code = ""
        last_version = None
        start_execution = datetime.now()
        
        while attempts < max_attempts:
            if (datetime.now() - start_execution).total_seconds() > 120:
                self.log("Global timeout reached", "error", True)
                break
            
            attempts += 1
            self.log(f"\n[Attempt {attempts}/{max_attempts}]", "info", False)

            prompt = (
                f"Develop a {language} code for: {description}"
                if attempts == 1
                else f"The previous code resulted in the error:\n{error_result}\nPlease correct the code and explain the correction."
            )
            if expected_output and attempts == 1:
                prompt += f"\nExpected output:\n{expected_output}"

            self.messages.append({"role": "user", "content": prompt})

            try:
                # Use the generic LLM client to generate the code
                response = self.llm_client.generate_completion(
                    messages=self.messages,
                    max_tokens=1500,
                    temperature=0
                )
                
                self.metrics_collector.update_metrics(response.tokens_used, False)
                
                generated_code = self.extract_code(response.content)
                if not generated_code:
                    self.log("No valid code found in response", "error", True)
                    error_result = "Response contains no valid code"
                    continue

                if self.trace:
                    self.log("\nExtracted Code:", "info")
                    self.log(generated_code, "info")

                last_version = generated_code
                
                # Save and execute code
                file_name = self.save_final_version(generated_code, language, "temp")
                result, error_result = self.execute_code(file_name, language)

                if error_result:
                    self.log(f"Error encountered:\n{error_result}", "error", self.trace)
                    previous_code = generated_code
                    self.metrics_collector.update_metrics(0, False, error_result)
                    continue

                if expected_output and expected_output.strip() != result.strip():
                    self.log(
                        f"Output mismatch:\nExpected: {expected_output}\nGot: {result}",
                        "warning",
                        self.trace
                    )
                    previous_code = generated_code
                    error_result = "Output mismatch"
                    continue

                # Success!
                self.log("\nCode generated successfully!", "info", True)
                if self.trace:
                    self.log(generated_code, "info")
                    self.metrics_collector.display_metrics(self.console)

                final_file_name = self.save_final_version(generated_code, language, "success")
                self.log(f"\nFinal code saved at: {final_file_name}", "info", True)
                
                # Clean up temporary files
                try:
                    if os.path.exists(file_name):
                        os.remove(file_name)
                except Exception as e:
                    self.log(f"Error cleaning temporary file: {str(e)}", "warning", False)
                
                return generated_code

            except Exception as e:
                error = self.error_handler.handle_error(e, "Error generating code")
                self.log(error, "error", True)
                self.metrics_collector.update_metrics(0, False, error)
                last_version = previous_code if previous_code else None

        # Finalization after attempts or timeout
        # self.log("Maximum attempts reached or timeout occurred.", "error", True)
        # if last_version:
        #     final_file_name = self.save_final_version(last_version, language, "failure")
        #     self.log(f"Last code version saved at: {final_file_name}", "info", True)
        
        # if self.trace:
        #     self.metrics_collector.display_metrics(self.console)
        # return None
            # Finalization after attempts or timeout
        self.log("Maximum attempts reached or timeout occurred.", "error", True)
        if last_version:
            final_file_name = self.save_final_version(last_version, language, "failure")
            self.log(f"Last code version saved at: {final_file_name}", "info", True)

        if self.trace:
            self.metrics_collector.display_metrics(self.console)
        
        # Retorna a última versão do código, mesmo que seja um fallback, se houver
        return last_version if last_version else None



def dscoder(
    description: str,
    language: str = "python",
    provider: str = "deepseek",
    model: Optional[str] = None,    
    trace: bool = False,
    timeout: int = 120,
    max_attempts: int = 5,
    expected_output: Optional[str] = None,
) -> Optional[str]:
    """
    Core function for generating code using AI models. This function provides a programmatic
    interface for the dscoder code generation capabilities.
    
    Available providers:
    - openai: OpenAI API (GPT-3.5, GPT-4)
    - anthropic: Anthropic API (Claude models)
    - deepseek: DeepSeek API
    - openrouter: OpenRouter API (access to multiple models)
    
    Args:
        description: Detailed description of the code to be generated. Should include:
                    - Required functionality
                    - Input/output specifications
                    - Any special requirements or constraints
        language: Target programming language. Supported options:
                 - "python" (default)
                 - "cpp" (C++)
                 - "r" (R)
                 - "julia"
                 - "rcpp" (Rcpp)
        provider: LLM provider to use. Supported options:
                 - "deepseek" (default)
                 - "openai"
                 - "anthropic"
                 - "openrouter"
        model: Specific model to use. If not provided, uses provider's default model.
               See README.md for supported models per provider.
        trace: Enable detailed logging and debugging output (default: False)
        timeout: Global timeout in seconds for code generation (default: 120)
        max_attempts: Maximum number of generation attempts (default: 5)
        expected_output: Expected output string for validation (optional). If provided,
                       the generated code will be executed and its output compared
                       against this value.
        
    Returns:
        Generated code as string if successful, None otherwise
        
    Raises:
        ValueError: For invalid input parameters
        RuntimeError: For execution failures or timeout
        
    Examples:
        Basic Python example:
        >>> code = dscoder(
        ...     description="Create a function to calculate factorial",
        ...     language="python",
        ...     expected_output="120"
        ... )
        
        C++ example with custom model:
        >>> code = dscoder(
        ...     description="Implement a linked list class",
        ...     language="cpp",
        ...     provider="openai",
        ...     model="gpt-4-turbo"
        ... )
        
        R example with tracing:
        >>> code = dscoder(
        ...     description="Create a function to calculate linear regression",
        ...     language="r",
        ...     trace=True
        ... )
        
    Notes:
        - For API key setup and configuration, see README.md
        - For troubleshooting and common patterns, see README.md
        - Code generation may take multiple attempts to produce valid results
        - Execution timeout includes both generation and validation time
        - Generated code is automatically validated when expected_output is provided
        
    See Also:
        main(): Command-line interface for dscoder
        AIAgent: Core implementation class
    """
    try:
        agent = AIAgent(provider=provider, trace=trace)
        return agent.generate_code(
            description=description,
            language=language,
            expected_output=expected_output,
            max_attempts=max_attempts
        )
    except Exception as e:
        raise RuntimeError(f"Code generation failed: {str(e)}") from e

def main():
    """Main function for command-line execution"""
    parser = ArgumentParser(description="AI Agent for code generation.")
    parser.add_argument(
        "description",
        type=str,
        help="Description of the code to be generated."
    )
    parser.add_argument(
        "--language",
        type=str,
        default="python",
        choices=["python", "cpp", "r", "julia", "rcpp"],
        help="Desired programming language."
    )
    parser.add_argument(
        "--expected_output",
        type=str,
        help="Expected output for the generated code.",
        default=None
    )
    parser.add_argument(
        "--provider",
        type=str,
        default="openrouter",
        choices=["openai", "anthropic", "deepseek", "openrouter"],  # Add openrouter
        help="LLM provider to use."
    )
    parser.add_argument(
        "--trace",
        action="store_true",
        help="Display detailed logs in the terminal."
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=120,
        help="Global timeout in seconds."
    )
    parser.add_argument(
        "--model",
        type=str,
        help="Specific model of the provider to use.",
        default=None
    )
    parser.add_argument(
        "--max_attempts",
        type=int,
        help="Specific max_attempts.",
        default=5
    )
    
    args = parser.parse_args()
    
    try:
        generated_code = dscoder(
            description=args.description,
            language=args.language,
            expected_output=args.expected_output,
            provider=args.provider,
            trace=args.trace,
            timeout=args.timeout,
            model=args.model,
            max_attempts = args.max_attempts
        )
        
        if generated_code:
            print("\nCode generation completed successfully!")
            print(generated_code)
        else:
            print("\nCode generation failed. Please check the logs for more details.")
            exit(1)
            
    except KeyboardInterrupt:
        print("\nOperation interrupted by the user.")
        exit(1)
    except Exception as e:
        print(f"\nFatal error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
