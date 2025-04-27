# DSCoder - Geração de Código Avançada Baseada em IA para Data Science

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) [![Python](https://img.shields.io/badge/python-3.8%2B-blue)]() [![Coverage](https://coveralls.io/repos/github/evandeilton/dscoder/badge.svg)]()

## Índice

- [Introdução](#introdução)
- [Funcionalidades Principais](#funcionalidades-principais)
- [Instalação e Configuração](#instalação-e-configuração)
- [Início Rápido](#início-rápido)
- [Arquitetura do Projeto](#arquitetura-do-projeto)
- [Interface do Usuário (UI)](#interface-do-usuário-ui)
- [Referência de Funções](#referência-de-funções)
- [Uso da Interface de Linha de Comando](#uso-da-interface-de-linha-de-comando)
- [Exemplos e Casos de Uso](#exemplos-e-casos-de-uso)
- [Melhores Práticas](#melhores-práticas)
- [Guia de Solução de Problemas](#guia-de-solução-de-problemas)
- [Diretrizes de Contribuição](#diretrizes-de-contribuição)
- [Licença e Créditos](#licença-e-créditos)
- [Informações de Contato](#informações-de-contato)

## Introdução

DSCoder é um sistema avançado de geração de código baseado em IA projetado para capacitar cientistas de dados, pesquisadores e desenvolvedores com a capacidade de gerar código de alta qualidade e pronto para produção para uma variedade de aplicações em data science e computação estatística. Ao aproveitar o poder dos large language models (LLMs), o DSCoder simplifica o processo de criação de código funcional, permitindo que os usuários se concentrem na resolução de problemas e inovação, em vez de gastar tempo com tarefas de codificação tediosas.

![dscoder em ação](assets/peek-dscoder-ex-01.gif)

DSCoder suporta múltiplas linguagens de programação, incluindo Python, R, Julia e C++, e integra-se com vários provedores de LLM, como OpenAI, Anthropic, DeepSeek e OpenRouter. Essa flexibilidade permite que os usuários escolham as melhores ferramentas para suas necessidades específicas e aproveitem os pontos fortes únicos de cada linguagem e provedor.

Seja você um cientista de dados experiente procurando automatizar a geração de código ou um pesquisador explorando novos algoritmos, o DSCoder fornece uma maneira eficiente e sem complicações de criar o código necessário para resolver problemas complexos.

## Funcionalidades Principais

### Linguagens de Programação Suportadas

| Linguagem | Casos de Uso Principais | Recursos Principais | Melhor Para |
|-----------|------------------------|-------------------|-------------|
| Python    | Data Science, ML | Integração de pacotes, Processamento de dados | Análise de dados geral |
| R/Rcpp    | Computação Estatística | Análise estatística, Computação de alto desempenho | Pesquisa estatística |
| Julia     | Computação Científica | Computação numérica, Otimização | Modelagem matemática |
| C++       | Computação de Performance | Otimização STL, Gerenciamento de memória | Operações em nível de sistema |

### Integração com Provedores

| Provedor   | Modelo Padrão | Modelos Alternativos | Pontos Fortes |
|------------|---------------|---------------------|---------------|
| DeepSeek   | deepseek-chat | deepseek-reasoner | Custo-benefício, Respostas rápidas |
| OpenAI     | gpt-4o        | gpt-4o-mini, o1-mini, o3-mini| Compreensão avançada |
| Anthropic  | claude-3-5-haiku-latest | claude-3-opus-20240229, claude-3-5-haiku-20241022 | Raciocínio complexo |
| OpenRouter | google/gemini-2.0-pro-exp-02-05:free | vários | Acesso a múltiplos modelos |

## Instalação e Configuração

### Pré-requisitos

- Python 3.8 ou superior
- Git
- Ferramenta de ambiente virtual (venv recomendado)
- Acesso às APIs dos provedores LLM

### Passos de Instalação

```bash
# Clone o repositório
git clone https://github.com/evandeilton/dscoder.git

# Navegue até o diretório do projeto
cd dscoder

# Crie e ative o ambiente virtual
python3 -m venv venv
source venv/bin/activate  # No Windows: .\venv\Scripts\Activate.ps1

# Instale as dependências
pip install -r requirements.txt
```

### Configuração da API

Para configurar as chaves de API como variáveis de ambiente:

| Plataforma   | Método de Configuração | Comando |
|--------------|----------------------|---------|
| Linux/macOS  | Adicionar ao ~/.bashrc ou ~/.zshrc | `export PROVIDER_API_KEY="sua_chave"` |
| Windows      | Definir variáveis de ambiente do usuário | `setx PROVIDER_API_KEY "sua_chave"` |

Chaves de API suportadas. Você pode configurar suas favoritas:

- DEEPSEEK_API_KEY
- OPENAI_API_KEY
- ANTHROPIC_API_KEY
- OPENROUTER_API_KEY

## Início Rápido

Para começar rapidamente com o DSCoder, siga estes passos:

1.  Clone o repositório e instale as dependências conforme descrito na seção Instalação e Configuração.
2.  Configure suas chaves de API como variáveis de ambiente.
3.  Use a função `dscoder()` para gerar código. Por exemplo:

```python
from dscoder import dscoder

code = dscoder(
    description="Criar uma função para calcular a média de uma lista",
    language="python"
)
print(code)
```

## Arquitetura do Projeto

O DSCoder é projetado com uma arquitetura modular para garantir flexibilidade e manutenibilidade. Os componentes principais do sistema incluem:

-   **`dscoder.py`:** Este módulo contém a lógica principal para geração de código. Inclui a função `dscoder()`, que serve como interface principal para os usuários interagirem com o sistema. Também define a classe `AIAgent`, que gerencia a interação com provedores LLM e lida com execução e validação de código.
-   **`llm_providers.py`:** Este módulo define a classe base abstrata `LLMProvider` e implementações concretas para diferentes provedores LLM, como OpenAI, Anthropic, DeepSeek e OpenRouter. Cada classe de provedor lida com a comunicação com a API LLM correspondente e padroniza as respostas.
-   **`ui.py`:** Este módulo fornece uma interface de usuário baseada em Streamlit para o DSCoder. Permite que os usuários interajam com o sistema através de uma interface gráfica, proporcionando uma experiência mais amigável.
-   **`setup.py`:** Este arquivo é usado para empacotar e distribuir o DSCoder como um pacote Python. Define os metadados do pacote, dependências e pontos de entrada.

## Interface do Usuário (UI)

O DSCoder fornece uma interface de usuário baseada em Streamlit (`ui.py`) que simplifica o processo de geração de código. A UI permite que os usuários:

-   Selecionem a linguagem de programação para geração de código.
-   Escolham o provedor LLM a ser usado.
-   Especifiquem o modelo a ser usado para geração de código.
-   Insiram uma descrição do código a ser gerado.
-   Visualizem o código gerado em um formato amigável.

A UI também fornece opções para configurar configurações avançadas, como habilitar registro detalhado, definir o timeout e especificar o número máximo de tentativas.

## Referência de Funções

### A Função `dscoder()`

A interface principal para geração de código é a função `dscoder()`:

```python
from dscoder import dscoder

code = dscoder(
    description="Sua descrição do código",
    language="python",
    provider="openrouter",
    model=None,
    trace=False,
    timeout=120,
    max_attempts=5,
    expected_output=None
)
```

#### Parâmetros

| Parâmetro      | Tipo | Padrão | Descrição |
|----------------|------|---------|-----------|
| description    | str  | Obrigatório | Requisitos detalhados para geração de código |
| language       | str  | "python" | Linguagem de programação alvo |
| provider       | str  | "openrouter" | Seleção do provedor LLM |
| model          | str  | None | Modelo específico a ser usado |
| trace          | bool | False | Habilitar registro detalhado |
| timeout        | int  | 120 | Timeout global em segundos |
| max_attempts   | int  | 5 | Número máximo de tentativas de retry |
| expected_output | str | None | Saída esperada para validação |
