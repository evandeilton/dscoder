# dscoder - AI Code Generation for Data Science

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)]()
[![Coverage](https://coveralls.io/repos/github/evandeilton/dscoder/badge.svg)]()

Advanced code generation system for data science and statistical computing, with support for Python, R, Julia, C++, and Rcpp.

## Installation

```bash
git clone https://github.com/evandeilton/dscoder.git
cd dscoder
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\Activate.ps1 on Windows
pip install -r requirements.txt
```

## Core Components

### AIAgent
Main interface for code generation:
```python
agent = AIAgent(
    provider="anthropic",  # LLM provider
    trace=True,           # Enable detailed logging
)
```

### LLMClient 
Manages provider interactions:
```python
from dscoder import LLMClient

client = LLMClient(provider="openai")
client.switch_provider("anthropic")  # Switch providers
```

### Code Generation

```python
code = agent.generate_code(
    description="Implementation request",
    language="python",          # python, r, julia, cpp, rcpp
    expected_output=None,       # Optional validation
    max_attempts=5             # Retry attempts
) -> Optional[str]
```

### Return Values

1. Success:
```python
code: str = agent.generate_code(...)  # Returns generated code
```

2. Failure:
```python
code: None = agent.generate_code(...)  # Returns None after max attempts
```

### File Structure

```
output/
├── code_success_20250123_153021.py  # Successful generations
├── code_failure_20250123_153045.r   # Failed attempts
├── temp/                            # Temporary files
│   └── code_temp_20250123_153032.py
└── logs/                            # Log directory
    └── ai_agent_20250123_153021.log
```

### Logging System

1. File Logging:
```
output/logs/ai_agent_YYYYMMDD_HHMMSS.log
```

2. Log Levels:
- INFO: Generation progress, milestones
- WARNING: Non-fatal issues, retries
- ERROR: Fatal errors, timeouts

3. Enable Detailed Logging:
```python
agent = AIAgent(trace=True)  # Terminal + file output
```

### Metrics Collection

Access runtime statistics:
```python
agent.metrics_collector.display_metrics()
```

Tracked Metrics:
- Token usage
- Success/failure counts
- Error occurrences
- Runtime stats

### Language Support

1. Python
```python
# Data science focus
code = agent.generate_code(
    description="Implement PCA with preprocessing",
    language="python"
)
```

2. R/Rcpp
```python
# Statistical computing
code = agent.generate_code(
    description="MCMC implementation",
    language="r"  # or "rcpp"
)
```

3. Julia
```python
# Numerical computing
code = agent.generate_code(
    description="Differential equations solver",
    language="julia"
)
```

4. C++
```python
# Performance computing
code = agent.generate_code(
    description="Optimized matrix operations",
    language="cpp"
)
```

### Provider Configuration

Set in `.env`:
```
OPENAI_API_KEY=your_key
ANTHROPIC_API_KEY=your_key
DEEPSEEK_API_KEY=your_key
```

### Error Handling

1. Runtime Errors:
```python
try:
    code = agent.generate_code(...)
except Exception as e:
    error = agent.error_handler.handle_error(e)
```

2. Execution Errors:
```python
result, error = agent.execute_code(file_path, language)
if error:
    print(f"Execution failed: {error}")
```

### Advanced Usage

1. Custom Timeouts:
```python
agent = AIAgent(
    provider="anthropic",
    timeout=120  # Global timeout
)
```

2. Output Validation:
```python
code = agent.generate_code(
    description="Sort array implementation",
    expected_output="[1, 2, 3, 4, 5]"
)
```

3. Provider Switching:
```python
agent.llm_client.switch_provider("openai")
```

4. Enhanced Logging:
```python
agent.log("Custom message", level="info", force=True)
```

### Best Practices

1. Code Generation:
- Provide detailed descriptions
- Specify expected outputs
- Use appropriate language selection
- Enable trace for debugging

2. Error Handling:
- Implement try-catch blocks
- Check execution results
- Monitor log files
- Review metrics

3. Performance:
- Use appropriate timeouts
- Consider token limits
- Monitor resource usage
- Cache results when possible

## License

MIT License - See LICENSE file