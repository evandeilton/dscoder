# dscoder - AI Code Generation Agent For Data Science Programming

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)]()
[![Build Status](https://img.shields.io/travis/evandeilton/dscoder)]()
[![Coverage Status](https://coveralls.io/repos/github/evandeilton/dscoder/badge.svg)]()

dscoder is a Python-based AI agent specialized in generating high-quality code across multiple programming languages. The agent supports Python, C++, R, Julia, and Rcpp, leveraging advanced language models to assist in code generation tasks.

## Features

- Multi-language code generation (Python, C++, R, Julia, Rcpp)
- Support for multiple LLM providers (OpenAI, Anthropic, DeepSeek)
- Error handling and code validation
- Execution environment management
- Detailed logging and metrics collection

## Installation

### Linux/MacOS
1. Clone the repository:
   ```bash
   git clone https://github.com/evandeilton/dscoder.git
   cd dscoder
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Windows
1. Install Python from [python.org](https://www.python.org/downloads/windows/)

2. Clone the repository:
   ```powershell
   git clone https://github.com/evandeilton/dscoder.git
   cd dscoder
   ```

3. Create and activate virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

4. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

## Usage Examples

### Python
```python
from dscoder import AgenteIA

# Initialize the agent
agent = AgenteIA(provider="openai")

# Generate code with error handling
try:
    generated_code = agent.gerar_codigo(
        descricao="Create a Python function to calculate Fibonacci sequence",
        linguagem="python"
    )
    print(generated_code)
except Exception as e:
    print(f"Error generating code: {e}")
```

### R
```r
library(dscoder)

# Initialize the agent
agent <- AgenteIA(provider="anthropic")

# Generate statistical analysis code
codigo <- gerar_codigo(
    descricao="Create R code to calculate mean and standard deviation",
    linguagem="r"
)
eval(parse(text=codigo))
```

### Julia
```julia
using dscoder

# Initialize the agent
agent = AgenteIA(provider="deepseek")

# Generate numerical computation code
codigo = gerar_codigo(
    descricao="Implement Newton-Raphson method in Julia",
    linguagem="julia"
)
eval(Meta.parse(codigo))
```

### C++
```cpp
#include <dscoder>

int main() {
    AgenteIA agent("openai");
    
    // Generate data structure implementation
    std::string codigo = agent.gerar_codigo(
        "Implement a binary tree in C++",
        "cpp"
    );
    
    // Execute generated code
    system(codigo.c_str());
    return 0;
}
```

## Configuration

### Obtaining API Keys
- [OpenAI API Keys](https://platform.openai.com/api-keys)
- [Anthropic API Keys](https://console.anthropic.com/settings/keys)
- [DeepSeek API Keys](https://platform.deepseek.com/api-keys)

Create a `.env` file with your API keys:
```
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
DEEPSEEK_API_KEY=your_deepseek_key
```

## Windows Support

### Common Windows Issues
1. **Permission Errors**:
   - Run PowerShell/Command Prompt as Administrator
   - Check execution policy: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`

2. **Path Length Limitations**:
   - Clone repository to a short path (e.g., C:\Projects)
   - Enable long path support in Windows

3. **Environment Variables**:
   - Set API keys through System Properties
   - Use `setx` command for persistent variables:
     ```cmd
     setx OPENAI_API_KEY "your_key_here"
     ```

## Contributing

Contributions are welcome! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Roadmap
- [ ] Add support for additional languages
- [ ] Implement code optimization features
- [ ] Add interactive debugging capabilities

## FAQ
**Q: How do I choose which LLM provider to use?**
A: Consider factors like cost, performance, and specific language support. OpenAI generally has the best Python support, while Anthropic may perform better for R.

**Q: Can I use multiple providers simultaneously?**
A: Yes, you can configure multiple API keys and switch between providers as needed.
