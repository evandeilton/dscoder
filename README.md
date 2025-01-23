# PyNinjaGitHub - AI Code Generation Agent

PyNinjaGitHub is a Python-based AI agent specialized in generating high-quality code across multiple programming languages. The agent supports Python, C++, R, Julia, and Rcpp, leveraging advanced language models to assist in code generation tasks.

## Features

- Multi-language code generation (Python, C++, R, Julia, Rcpp)
- Support for multiple LLM providers (OpenAI, Anthropic, DeepSeek)
- Error handling and code validation
- Execution environment management
- Detailed logging and metrics collection

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/PyNinjaGitHub.git
   cd PyNinjaGitHub
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

```python
from agent import AgenteIA

# Initialize the agent
agent = AgenteIA(provider="openai")

# Generate code
generated_code = agent.gerar_codigo(
    descricao="Create a Python function to calculate Fibonacci sequence",
    linguagem="python"
)

print(generated_code)
```

## Configuration

Create a `.env` file with your API keys:
```
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
DEEPSEEK_API_KEY=your_deepseek_key
```

## Contributing

Contributions are welcome! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
