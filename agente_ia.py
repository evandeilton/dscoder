# Sistema de arquivos e ambiente
import os
import subprocess
import logging
from pathlib import Path
from datetime import datetime
import re
import tempfile
import shutil

# Argumentos e ambiente
from argparse import ArgumentParser
from dotenv import load_dotenv

# Tipos
from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass

# UI
from rich.console import Console
from rich.table import Table
from rich.logging import RichHandler

# APIs de LLM
from openai import OpenAI
from anthropic import Anthropic

class ErrorHandler:
    """Gerenciador de erros do sistema"""
    
    def __init__(self):
        self.console = Console()
        
    def handle_error(self, error: Exception, context: str = "") -> str:
        """
        Processa e formata erros do sistema
        
        Args:
            error: Exceção capturada
            context: Contexto adicional do erro
            
        Returns:
            str: Mensagem de erro formatada
        """
        error_msg = f"{type(error).__name__}: {str(error)}"
        if context:
            error_msg = f"{context}: {error_msg}"
        return error_msg

class MetricsCollector:
    """Coletor de métricas de execução"""
    
    def __init__(self):
        self.total_tokens = 0
        self.successful_generations = 0
        self.failed_generations = 0
        self.errors = []
        
    def update_metrics(self, tokens: int, success: bool, error: str = None):
        """Atualiza métricas de execução"""
        self.total_tokens += tokens
        if success:
            self.successful_generations += 1
        else:
            self.failed_generations += 1
            if error:
                self.errors.append(error)
    
    def display_metrics(self, console: Console):
        """Exibe métricas em uma tabela formatada"""
        table = Table(title="Métricas de Execução")
        table.add_column("Métrica", style="cyan")
        table.add_column("Valor", style="magenta")
        
        table.add_row("Total de Tokens", str(self.total_tokens))
        table.add_row("Gerações com Sucesso", str(self.successful_generations))
        table.add_row("Gerações com Falha", str(self.failed_generations))
        table.add_row("Total de Erros", str(len(self.errors)))
        
        console.print(table)

@dataclass
class LLMResponse:
    """Classe para padronizar a resposta dos diferentes providers de LLM"""
    content: str
    tokens_used: int
    model: str
    provider: str

class LLMProvider(ABC):
    """Classe abstrata base para providers de LLM"""
    
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
    """Provider para OpenAI"""
    
    def __init__(self):
        self.client = None
        self.default_model = "gpt-4"
    
    def initialize_client(self) -> None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY não encontrada nas variáveis de ambiente")
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
    """Provider para Anthropic"""
    
    def __init__(self):
        self.client = None
        self.default_model = "claude-3-5-sonnet-20241022"
    
    def initialize_client(self) -> None:
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY não encontrada nas variáveis de ambiente")
        self.client = Anthropic(api_key=api_key)
    
    def _convert_messages(self, messages: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """Converte mensagens do formato OpenAI para Anthropic"""
        converted = []
        for msg in messages:
            role = msg["role"]
            content = msg["content"]
            if role == "system":
                converted.append({"role": "assistant", "content": content})
            elif role in ["user", "assistant"]:
                converted.append({"role": role, "content": content})
            else:
                logging.warning(f"Tipo de mensagem não suportado: {role}")
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
    Provider para a API DeepSeek que utiliza a mesma interface da OpenAI.
    
    Atributos:
        client: Cliente OpenAI configurado para a API DeepSeek
        default_model: Modelo padrão da DeepSeek a ser usado
        base_url: URL base da API DeepSeek
    """
    
    def __init__(self):
        self.client = None
        self.default_model = "deepseek-chat"
        self.base_url = "https://api.deepseek.com"
    
    def initialize_client(self) -> None:
        """
        Inicializa o cliente OpenAI com as configurações da DeepSeek.
        
        Raises:
            ValueError: Se a DEEPSEEK_API_KEY não estiver definida nas variáveis de ambiente
        """
        api_key = os.getenv("DEEPSEEK_API_KEY")
        if not api_key:
            raise ValueError("DEEPSEEK_API_KEY não encontrada nas variáveis de ambiente")
            
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
        Gera uma completação usando a API DeepSeek.
        
        Args:
            messages: Lista de mensagens no formato OpenAI
            max_tokens: Número máximo de tokens na resposta
            temperature: Temperatura para geração (criatividade)
            model: Modelo específico a ser usado (opcional)
            
        Returns:
            LLMResponse: Resposta padronizada contendo o conteúdo gerado e metadados
            
        Raises:
            RuntimeError: Se o cliente não estiver inicializado
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


class LLMClient:
    """Cliente genérico para LLMs que gerencia diferentes providers"""
    
    def __init__(self, provider: str = "openai"):
        load_dotenv()
        self.providers = {
            "openai": OpenAIProvider(),
            "anthropic": AnthropicProvider(),
            "deepseek": DeepSeekProvider()
        }
        
        if provider not in self.providers:
            raise ValueError(f"Provider {provider} não suportado")
            
        self.current_provider = self.providers[provider]
        self.current_provider.initialize_client()
    
    def switch_provider(self, provider: str) -> None:
        if provider not in self.providers:
            raise ValueError(f"Provider {provider} não suportado")
        self.current_provider = self.providers[provider]
        self.current_provider.initialize_client()
    
    def generate_completion(
        self,
        messages: List[Dict[str, str]],
        max_tokens: int = 2500,
        temperature: float = 0,
        model: Optional[str] = None
    ) -> LLMResponse:
        return self.current_provider.generate_completion(
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
            model=model
        )

class AgenteIA:
    def __init__(self, provider: str = "openai", trace: bool = False):
        """Inicializa o agente de IA"""
        self.llm_client = LLMClient(provider)
        self.trace = trace
        self.console = Console()
        self.error_handler = ErrorHandler()
        self.metrics_collector = MetricsCollector()
        
        # Configuração de diretórios
        self.base_dir = Path("output")
        self.temp_dir = self.base_dir / "temp"
        self.logs_dir = self.base_dir / "logs"
        
        for dir_path in [self.base_dir, self.temp_dir, self.logs_dir]:
            dir_path.mkdir(parents=True, exist_ok=True)
        
        # Configuração de logging
        log_format = "%(asctime)s [%(levelname)s] %(message)s"
        log_file = self.logs_dir / f"agente_ia_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        
        logging.basicConfig(
            level=logging.INFO,
            format=log_format,
            handlers=[
                logging.FileHandler(log_file, encoding='utf-8'),
                RichHandler(rich_tracebacks=True)
            ]
        )
        self.logger = logging.getLogger(__name__)
        
        # Inicialização das mensagens
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
                    "ALL mentioned or used functions MUST be implemented in the same code block. "
                    "For C++, use EXCLUSIVELY STL native resources."
                )
            }
        ]
    
    def log(self, message: str, level: str = "info", force: bool = False):
        """Registra mensagens de log"""
        if self.trace or force:
            if level == "error":
                self.logger.error(message)
            elif level == "warning":
                self.logger.warning(message)
            else:
                self.logger.info(message)    

    def extrair_codigo(self, content: str) -> Optional[str]:
        """
        Extrai código da resposta do LLM, com suporte para múltiplas linguagens (R, Python, Julia, C++/Rcpp)
        e validação de conteúdo.
        
        Args:
            self: Instância da classe
            content (str): Conteúdo completo da resposta do LLM
            
        Returns:
            Optional[str]: Código extraído ou None se nenhum código válido for encontrado
        """
        # Linguagens suportadas e seus padrões
        language_patterns: Dict[str, List[str]] = {
            'r': [r'library\(', r'function\(', r'<-', r'%>%'],
            'python': [r'import\s+\w+', r'def\s+\w+\(', r'class\s+\w+:'],
            'julia': [r'using\s+\w+', r'function\s+\w+\(', r'struct\s+\w+'],
            'cpp': [r'#include', r'void\s+\w+\(', r'int\s+\w+\(', r'class\s+\w+\s*\{'],
            'rcpp': [r'//\[\[Rcpp::export\]\]', r'NumericVector', r'DataFrame']
        }
        
        # Frases comuns que não são código
        common_phrases = [
            'vou criar', 'vou fornecer', 'aqui está', 'segue', 
            'exemplo', 'podemos', 'você pode', 'agora'
        ]
        
        def detect_language(code: str) -> Optional[str]:
            """Detecta a linguagem do código baseado em padrões específicos."""
            code = code.lower()
            for lang, patterns in language_patterns.items():
                if any(re.search(pattern, code, re.IGNORECASE) for pattern in patterns):
                    return lang
            return None
        
        def validate_code_block(code: str) -> bool:
            """Valida se o bloco extraído é realmente código."""
            # Remove espaços em branco
            code = code.strip()
            
            # Verifica se o bloco está vazio
            if not code:
                return False
                
            # Verifica frases comuns que não são código
            if any(code.lower().startswith(phrase) for phrase in common_phrases):
                return False
            
            # Verifica caracteres comuns em código
            code_indicators = ['(', ')', '{', '}', '=', ':', ';', '#', '"', "'"]
            if not any(indicator in code for indicator in code_indicators):
                return False
                
            # Verifica se parece ser código de alguma linguagem suportada
            return detect_language(code) is not None
        
        # Procura por blocos de código markdown com especificação de linguagem
        matches = re.finditer(r'```(\w*)\n(.*?)```', content, re.DOTALL)
        
        # Lista para armazenar blocos válidos
        valid_blocks = []
        
        # Processa cada match encontrado
        for match in matches:
            lang, code = match.groups()
            code = code.strip()
            
            # Se a linguagem foi especificada no markdown, verifica se é suportada
            if lang and lang.lower() not in language_patterns:
                continue
                
            # Valida o bloco de código
            if validate_code_block(code):
                valid_blocks.append(code)
        
        # Retorna o primeiro bloco válido encontrado ou None
        return valid_blocks[0] if valid_blocks else None
    
    def salvar_versao_final(self, codigo: str, linguagem: str, status: str) -> str:
        """Salva versão final do código gerado"""
        extensoes = {
            "python": ".py",
            "cpp": ".cpp",
            "r": ".R",
            "julia": ".jl",
            "rcpp": ".cpp"
        }
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        ext = extensoes.get(linguagem.lower(), ".txt")
        filename = f"codigo_{status}_{timestamp}{ext}"
        
        if status == "temp":
            filepath = self.temp_dir / filename
        else:
            filepath = self.base_dir / filename
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(codigo)
        
        return str(filepath)
    
    def executar_codigo(self, arquivo: str, linguagem: str) -> Tuple[str, Optional[str]]:
        """Executa o código gerado"""
        comandos = {
            "python": ["python", arquivo],
            "cpp": ["g++", arquivo, "-o", arquivo + ".exe"],
            "r": ["Rscript", arquivo],
            "julia": ["julia", arquivo],
            "rcpp": ["R", "CMD", "SHLIB", arquivo]
        }
        
        if linguagem.lower() not in comandos:
            return "", f"Linguagem não suportada: {linguagem}"
        
        try:
            processo = subprocess.Popen(
                comandos[linguagem.lower()],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            stdout, stderr = processo.communicate(timeout=30)
            
            if processo.returncode != 0:
                return "", stderr
            
            return stdout, None
            
        except subprocess.TimeoutExpired:
            return "", "Timeout na execução do código"
        except Exception as e:
            return "", str(e)
    
    def gerar_codigo(
        self,
        descricao: str,
        linguagem: str = "python",
        output_esperado: Optional[str] = None,
        max_tentativas: int = 5
    ) -> Optional[str]:
        """Gera código com base na descrição fornecida"""
        tentativas = 0
        codigo_anterior = ""
        resultado_erro = ""
        codigo_gerado = ""
        ultima_versao = None
        inicio_execucao = datetime.now()
        
        while tentativas < max_tentativas:
            if (datetime.now() - inicio_execucao).total_seconds() > 120:
                self.log("Timeout global atingido", "error", True)
                break
                
            tentativas += 1
            self.log(f"\n[Tentativa {tentativas}/{max_tentativas}]", "info", False)

            prompt = (
                f"Desenvolva um código em {linguagem} para: {descricao}"
                if tentativas == 1
                else f"O código anterior apresentou o erro:\n{resultado_erro}\nPor favor, corrija o código e explique a correção."
            )
            if output_esperado and tentativas == 1:
                prompt += f"\nOutput esperado:\n{output_esperado}"

            self.messages.append({"role": "user", "content": prompt})

            try:
                # Usa o cliente LLM genérico para gerar o código
                resposta = self.llm_client.generate_completion(
                    messages=self.messages,
                    max_tokens=1500,
                    temperature=0
                )
                
                self.metrics_collector.update_metrics(resposta.tokens_used, False)
                
                codigo_gerado = self.extrair_codigo(resposta.content)
                if not codigo_gerado:
                    self.log("Nenhum código válido encontrado na resposta", "error", True)
                    resultado_erro = "Resposta sem código válido"
                    continue

                if self.trace:
                    self.log("\nCódigo extraído:", "info")
                    self.log(codigo_gerado, "info")

                ultima_versao = codigo_gerado
                
                # Salva e executa código
                nome_arquivo = self.salvar_versao_final(codigo_gerado, linguagem, "temp")
                resultado, resultado_erro = self.executar_codigo(nome_arquivo, linguagem)

                if resultado_erro:
                    self.log(f"Erro encontrado:\n{resultado_erro}", "error", self.trace)
                    codigo_anterior = codigo_gerado
                    self.metrics_collector.update_metrics(0, False, resultado_erro)
                    continue

                if output_esperado and output_esperado.strip() != resultado.strip():
                    self.log(
                        f"Output divergente:\nEsperado: {output_esperado}\nObtido: {resultado}",
                        "warning",
                        self.trace
                    )
                    codigo_anterior = codigo_gerado
                    resultado_erro = "Output divergente"
                    continue

                # Sucesso!
                self.log("\nCódigo gerado com sucesso!", "info", True)
                if self.trace:
                    self.log(codigo_gerado, "info")
                    self.metrics_collector.display_metrics(self.console)

                nome_arquivo_final = self.salvar_versao_final(codigo_gerado, linguagem, "sucesso")
                self.log(f"\nCódigo final salvo em: {nome_arquivo_final}", "info", True)
                
                # Limpeza dos arquivos temporários
                try:
                    if os.path.exists(nome_arquivo):
                        os.remove(nome_arquivo)
                except Exception as e:
                    self.log(f"Erro ao limpar arquivo temporário: {str(e)}", "warning", False)
                
                return codigo_gerado

            except Exception as e:
                erro = self.error_handler.handle_error(e, "Erro na geração de código")
                self.log(erro, "error", True)
                self.metrics_collector.update_metrics(0, False, erro)
                ultima_versao = codigo_anterior if codigo_anterior else None

        # Finalização após tentativas ou timeout
        self.log("Número máximo de tentativas atingido ou timeout.", "error", True)
        if ultima_versao:
            nome_arquivo_final = self.salvar_versao_final(ultima_versao, linguagem, "falha")
            self.log(f"Última versão do código salva em: {nome_arquivo_final}", "info", True)
        
        if self.trace:
            self.metrics_collector.display_metrics(self.console)
        return None


def main():
    """Função principal para execução via linha de comando"""
    parser = ArgumentParser(description="Agente de IA para geração de códigos.")
    parser.add_argument(
        "descricao",
        type=str,
        help="Descrição do código a ser gerado."
    )
    parser.add_argument(
        "--linguagem",
        type=str,
        default="python",
        choices=["python", "cpp", "r", "julia", "rcpp"],
        help="Linguagem de programação desejada."
    )
    parser.add_argument(
        "--output_esperado",
        type=str,
        help="Output esperado para o código gerado.",
        default=None
    )
    parser.add_argument(
        "--provider",
        type=str,
        default="openai",
        choices=["openai", "anthropic","deepseek"],
        help="Provider LLM a ser usado."
    )
    parser.add_argument(
        "--trace",
        action="store_true",
        help="Exibir logs detalhados no terminal."
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=120,
        help="Timeout global em segundos."
    )
    parser.add_argument(
        "--model",
        type=str,
        help="Modelo específico do provider a ser usado.",
        default=None
    )
    
    args = parser.parse_args()
    
    try:
        agente = AgenteIA(provider=args.provider, trace=args.trace)
        codigo_gerado = agente.gerar_codigo(
            descricao=args.descricao,
            linguagem=args.linguagem,
            output_esperado=args.output_esperado
        )
        
        if codigo_gerado:
            print("\nGeração de código concluída com sucesso!")
        else:
            print("\nFalha na geração do código. Verifique os logs para mais detalhes.")
            exit(1)
            
    except KeyboardInterrupt:
        print("\nOperação interrompida pelo usuário.")
        exit(1)
    except Exception as e:
        print(f"\nErro fatal: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
