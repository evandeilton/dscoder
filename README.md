# dscoder - AI Code Generation for Data Science

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) [![Python](https://img.shields.io/badge/python-3.8%2B-blue)]() [![Coverage](https://coveralls.io/repos/github/evandeilton/dscoder/badge.svg)]()

**dscoder** is an advanced AI-powered code generation system tailored for data science and statistical computing. It supports multiple programming languages, including Python, R, Julia, C++, and Rcpp, enabling seamless integration into your data workflows.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Jupyter Notebook](#jupyter-notebook-usage)
    <!-- - [Basic Setup](#basic-setup)
    - [Language-Specific Examples](#language-specific-examples)
      - [Python](#python-examples)
      - [R](#r-examples)
      - [Julia](#julia-examples)
      - [C++](#cpp-examples) -->
  - [Terminal](#terminal-usage)
    <!-- - [Python Scripts](#python-script-examples)
    - [Provider Configuration](#provider-examples)
    - [Advanced Usage](#advanced-examples)
    - [Command Line Interface](#command-line-interface) -->
- [Common Patterns](#common-patterns)
  - [Data Science Pipeline](#data-science-pipeline)
  - [Statistical Analysis](#statistical-analysis)
- [FAQ](#faq)
  <!-- - [API Key Setup](#key-setup)
  - [General Usage](#usage)
  - [Troubleshooting](#common-issues)
  - [Features](#features-1)
  - [Examples](#examples)
  - [Support](#support) -->
- [License](#license)

## Features

- **Multi-Language Support**: Generate code in Python, R, Julia, C++, and Rcpp.
- **Versatile Integration**: Compatible with Jupyter Notebooks and terminal environments.
- **Multiple Providers**: Choose between DeepSeek (default), OpenAI, and Anthropic for code generation.
- **Advanced Capabilities**:
  - Output validation
  - Error handling
  - Metrics collection
  - Customizable timeouts and attempts

## Installation

To install **dscoder**, follow these steps:

```bash
git clone https://github.com/evandeilton/dscoder.git
cd dscoder
python3 -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Usage

### Jupyter Notebook Usage

#### Basic Setup

Start by importing and initializing the `AIAgent`:

```python
# Import the AIAgent from dscoder
from dscoder import AIAgent

# Initialize with DeepSeek (default provider)
agent = AIAgent()
```

#### Language-Specific Examples

##### Python Examples

**Data Analysis**

```python
code = agent.generate_code("""
Create a function that:
1. Reads a CSV file
2. Handles missing values
3. Calculates descriptive statistics
4. Creates visualizations with seaborn
""")
```

**Machine Learning**

```python
code = agent.generate_code("""
Implement a RandomForest classifier with:
1. Cross-validation
2. Hyperparameter tuning
3. Feature importance plot
4. Confusion matrix
""")
```

**Time Series**

```python
code = agent.generate_code("""
Create an ARIMA model implementation:
1. Data preprocessing
2. Model selection
3. Forecasting
4. Accuracy metrics
""")
```

##### R Examples

**Statistical Analysis**

```python
code = agent.generate_code(
    """
    Create comprehensive statistical analysis:
    1. Load and clean data
    2. Normality tests
    3. ANOVA
    4. Post-hoc tests
    5. Visualization
    """,
    language="r"
)
```

**Mixed Models**

```python
code = agent.generate_code(
    """
    Implement a linear mixed model:
    1. Random effects
    2. Fixed effects
    3. Model diagnostics
    """,
    language="r"
)
```

##### Julia Examples

**Numerical Computing**

```python
code = agent.generate_code(
    """
    Implement a differential equations solver:
    1. Runge-Kutta method
    2. Error estimation
    3. Plotting solution
    """,
    language="julia"
)
```

**Optimization**

```python
code = agent.generate_code(
    """
    Create an optimization algorithm:
    1. Gradient descent
    2. Convergence check
    3. Visualization
    """,
    language="julia"
)
```

##### C++ Examples

**Data Structures**

```python
code = agent.generate_code(
    """
    Implement a Red-Black Tree:
    1. Insertion
    2. Deletion
    3. Balancing
    4. Search
    """,
    language="cpp"
)
```

**Algorithms**

```python
code = agent.generate_code(
    """
    Create sorting algorithms:
    1. QuickSort
    2. MergeSort
    3. Performance comparison
    """,
    language="cpp"
)
```

### Terminal Usage

#### Python Script Examples

Create a Python script (e.g., `generate_ml.py`) to generate machine learning code:

```python
from dscoder import AIAgent

def main():
    agent = AIAgent(trace=True)
    
    code = agent.generate_code(
        description="Implement gradient boosting classifier",
        language="python",
        expected_output="Classification report"
    )
    
    if code:
        print("Code generated successfully!")
        print(code)

if __name__ == "__main__":
    main()
```

Run the script:

```bash
python generate_ml.py
```

#### Provider Examples

Switch between different AI providers:

```python
# Using OpenAI
agent = AIAgent(provider="openai")
code = agent.generate_code("Implement PCA dimensionality reduction")

# Using Anthropic
agent = AIAgent(provider="anthropic")
code = agent.generate_code("Create clustering algorithm")

# Using DeepSeek (default)
agent = AIAgent()  # or provider="deepseek"
code = agent.generate_code("Build neural network classifier")
```

#### Advanced Examples

**Custom Timeout**

```python
agent = AIAgent(timeout=180)
```

**Output Validation**

```python
code = agent.generate_code(
    description="Sort numbers [5,2,8,1,9]",
    expected_output="[1,2,5,8,9]"
)
```

**Error Handling**

```python
try:
    code = agent.generate_code(
        description="Complex task",
        max_attempts=10
    )
except Exception as e:
    print(f"Error: {e}")
```

**Metrics Collection**

```python
agent.metrics_collector.display_metrics()
```

#### Command Line Interface

Generate code directly from the terminal:

```bash
# Basic usage
python -m dscoder "Create function to calculate correlation matrix"

# Specify language
python -m dscoder "Implement binary search tree" --language cpp

# Enable tracing
python -m dscoder "Statistical analysis" --trace

# Set provider
python -m dscoder "Machine learning model" --provider anthropic
```

## Common Patterns

### Data Science Pipeline

Streamline your data science workflow with these steps:

```python
# 1. Data Loading
code = agent.generate_code("Load and preprocess CSV data")

# 2. Feature Engineering
code = agent.generate_code("Create feature engineering pipeline")

# 3. Model Training
code = agent.generate_code("Train ML model with cross-validation")

# 4. Evaluation
code = agent.generate_code("Generate model evaluation metrics")
```

### Statistical Analysis

Conduct comprehensive statistical analyses:

```python
# 1. Descriptive Statistics
code = agent.generate_code(
    "Calculate comprehensive descriptive statistics",
    language="r"
)

# 2. Hypothesis Testing
code = agent.generate_code(
    "Perform t-tests and chi-square tests",
    language="r"
)

# 3. Visualization
code = agent.generate_code(
    "Create statistical visualizations",
    language="r"
)
```

## FAQ

### API Key Setup

**Q: Where do I get API keys?**

- **DeepSeek**: [platform.deepseek.com/api-keys](https://platform.deepseek.com/api-keys)
- **OpenAI**: [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
- **Anthropic**: [console.anthropic.com/settings/keys](https://console.anthropic.com/settings/keys)

**Q: How do I set up API keys?**

To apply API keys on Linux and Windows:

**Linux (local user)**
```bash
# Add to ~/.bashrc or ~/.zshrc
echo 'export DEEPSEEK_API_KEY="your_key"' >> ~/.bashrc
echo 'export OPENAI_API_KEY="your_key"' >> ~/.bashrc
echo 'export ANTHROPIC_API_KEY="your_key"' >> ~/.bashrc

# Apply changes
source ~/.bashrc
```

**Windows (user environment variables)**
```powershell

# Command Prompt (run as user)
setx DEEPSEEK_API_KEY "your_key"
setx OPENAI_API_KEY "your_key"
setx ANTHROPIC_API_KEY "your_key"
```

**Verify Keys**
```python
import os
print(os.getenv('DEEPSEEK_API_KEY'))
print(os.getenv('OPENAI_API_KEY'))
print(os.getenv('ANTHROPIC_API_KEY'))
```

### General Usage

**Q: How do I generate basic code?**

```python
from dscoder import AIAgent

agent = AIAgent()
code = agent.generate_code("Calculate mean and standard deviation")
print(code)
```

**Q: Where is my generated code saved?**

Generated code is saved in the `output/` directory:

```
output/
├── code_success_*.py  # Successfully generated code
├── code_failure_*.py  # Failed attempts
└── logs/              # Debug information
```

**Q: Can I specify the programming language?**

Yes, specify the language using the `language` parameter:

```python
# Available languages: python, r, julia, cpp, rcpp
code = agent.generate_code(
    description="Sort array",
    language="python"
)
```

### Troubleshooting

**Q: Code generation fails?**

- **Check API keys**: Ensure your API keys are correctly set in the `.env` file.
- **Increase timeout**: Initialize the agent with a higher timeout.
  ```python
  agent = AIAgent(timeout=180)
  ```
- **Enable tracing**: Activate tracing to get detailed logs.
  ```python
  agent = AIAgent(trace=True)
  ```
- **Check logs**: Review logs in the `output/logs/` directory for more information.

**Q: How do I handle timeouts?**

Configure timeout settings and maximum attempts:

```python
agent = AIAgent(
    timeout=180,
    max_attempts=10
)
```

**Q: Provider not responding?**

Switch to a different AI provider:

```python
# Switch to OpenAI
agent.llm_client.switch_provider("openai")
```

### Features

**Q: What languages are supported?**

- **Python (`python`)**: Ideal for data science and machine learning.
- **R/Rcpp (`r`)**: Perfect for statistical analysis.
- **Julia (`julia`)**: Suitable for numerical computing.
- **C++ (`cpp`)**: Best for performance-critical applications.

**Q: Can I validate outputs?**

Yes, specify the expected output to validate the generated code:

```python
code = agent.generate_code(
    description="Sort [5,1,3]",
    expected_output="[1,3,5]"
)
```

**Q: How do I monitor usage?**

Display collected metrics using:

```python
agent.metrics_collector.display_metrics()
```

### Examples

**Q: How do I generate ML code?**

```python
code = agent.generate_code("""
1. Load iris dataset
2. Train RandomForest
3. Print accuracy
""")
print(code)
```

**Q: Statistical analysis in R?**

```python
code = agent.generate_code(
    """
    1. Load mtcars dataset
    2. Run ANOVA
    3. Plot results
    """,
    language="r"
)
print(code)
```

**Q: Numerical computing in Julia?**

```python
code = agent.generate_code(
    "Implement gradient descent",
    language="julia"
)
print(code)
```

### Support

**Q: Where do I get help?**

- **Issues**: [github.com/evandeilton/dscoder/issues](https://github.com/evandeilton/dscoder/issues)
- **Documentation**: [github.com/evandeilton/dscoder/docs](https://github.com/evandeilton/dscoder/docs)
- **API Documentation**:
  - **DeepSeek**: [platform.deepseek.com/docs](https://platform.deepseek.com/docs)
  - **OpenAI**: [platform.openai.com/docs](https://platform.openai.com/docs)
  - **Anthropic**: [docs.anthropic.com/claude](https://docs.anthropic.com/claude)

## License

This project is licensed under the [MIT License](LICENSE).

















<!-- # dscoder - AI Code Generation for Data Science

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)]()
[![Coverage](https://coveralls.io/repos/github/evandeilton/dscoder/badge.svg)]()

Advanced code generation system for data science and statistical computing, with support for Python, R, Julia, C++, and Rcpp.

## Installation

```bash
git clone https://github.com/evandeilton/dscoder.git
cd dscoder
python3 -m venv venv
source venv/bin/activate  # or .\venv\Scripts\Activate.ps1 on Windows
pip install -r requirements.txt
```

## Jupyter Notebook Usage

### Basic Setup
```python
# import sys
# sys.path.append("path/to/dscoder")
from dscoder import AIAgent

# Initialize with DeepSeek (default)
agent = AIAgent()
```

### Python Examples

```python
# Data Analysis
code = agent.generate_code("""
Create a function that:
1. Reads a CSV file
2. Handles missing values
3. Calculates descriptive statistics
4. Creates visualizations with seaborn
""")

# Machine Learning
code = agent.generate_code("""
Implement RandomForest classifier with:
1. Cross-validation
2. Hyperparameter tuning
3. Feature importance plot
4. Confusion matrix
""")

# Time Series
code = agent.generate_code("""
Create ARIMA model implementation:
1. Data preprocessing
2. Model selection
3. Forecasting
4. Accuracy metrics
""")
```

### R Examples

```python
# Statistical Analysis
code = agent.generate_code(
    """
    Create comprehensive statistical analysis:
    1. Load and clean data
    2. Normality tests
    3. ANOVA
    4. Post-hoc tests
    5. Visualization
    """,
    language="r"
)

# Mixed Models
code = agent.generate_code(
    """
    Implement linear mixed model:
    1. Random effects
    2. Fixed effects
    3. Model diagnostics
    """,
    language="r"
)
```

### Julia Examples

```python
# Numerical Computing
code = agent.generate_code(
    """
    Implement differential equations solver:
    1. Runge-Kutta method
    2. Error estimation
    3. Plotting solution
    """,
    language="julia"
)

# Optimization
code = agent.generate_code(
    """
    Create optimization algorithm:
    1. Gradient descent
    2. Convergence check
    3. Visualization
    """,
    language="julia"
)
```

### C++ Examples

```python
# Data Structures
code = agent.generate_code(
    """
    Implement Red-Black Tree:
    1. Insertion
    2. Deletion
    3. Balancing
    4. Search
    """,
    language="cpp"
)

# Algorithms
code = agent.generate_code(
    """
    Create sorting algorithms:
    1. QuickSort
    2. MergeSort
    3. Performance comparison
    """,
    language="cpp"
)
```

## Terminal Usage

### Python Script Examples

```python
# save as generate_ml.py
from dscoder import AIAgent

def main():
    agent = AIAgent(trace=True)
    
    code = agent.generate_code(
        description="Implement gradient boosting classifier",
        language="python",
        expected_output="Classification report"
    )
    
    if code:
        print("Code generated successfully!")
        
if __name__ == "__main__":
    main()
```

### Provider Examples

```python
# OpenAI
agent = AIAgent(provider="openai")
code = agent.generate_code(
    "Implement PCA dimensionality reduction"
)

# Anthropic
agent = AIAgent(provider="anthropic")
code = agent.generate_code(
    "Create clustering algorithm"
)

# DeepSeek (default)
agent = AIAgent()  # or provider="deepseek"
code = agent.generate_code(
    "Build neural network classifier"
)
```

### Advanced Examples

```python
# Custom Timeout
agent = AIAgent(timeout=180)

# Output Validation
code = agent.generate_code(
    description="Sort numbers [5,2,8,1,9]",
    expected_output="[1,2,5,8,9]"
)

# Error Handling
try:
    code = agent.generate_code(
        description="Complex task",
        max_attempts=10
    )
except Exception as e:
    print(f"Error: {e}")

# Metrics Collection
agent.metrics_collector.display_metrics()
```

### Command Line Interface

```bash
# Basic usage
python -m dscoder "Create function to calculate correlation matrix"

# Specify language
python -m dscoder "Implement binary search tree" --language cpp

# Enable tracing
python -m dscoder "Statistical analysis" --trace

# Set provider
python -m dscoder "Machine learning model" --provider anthropic
```

## Common Patterns

### Data Science Pipeline
```python
# 1. Data Loading
code = agent.generate_code("Load and preprocess CSV data")

# 2. Feature Engineering
code = agent.generate_code("Create feature engineering pipeline")

# 3. Model Training
code = agent.generate_code("Train ML model with cross-validation")

# 4. Evaluation
code = agent.generate_code("Generate model evaluation metrics")
```

### Statistical Analysis
```python
# 1. Descriptive Statistics
code = agent.generate_code(
    "Calculate comprehensive descriptive statistics",
    language="r"
)

# 2. Hypothesis Testing
code = agent.generate_code(
    "Perform t-tests and chi-square tests",
    language="r"
)

# 3. Visualization
code = agent.generate_code(
    "Create statistical visualizations",
    language="r"
)
```


# FAQ

## KEY Setup

**Q: Where do I get API keys?**
- DeepSeek: platform.deepseek.com/api-keys
- OpenAI: platform.openai.com/api-keys
- Anthropic: console.anthropic.com/settings/keys

**Q: How do I set up API keys?**
Create `.env` file:
```bash
DEEPSEEK_API_KEY=your_key
OPENAI_API_KEY=your_key
ANTHROPIC_API_KEY=your_key
```

**Q: Which provider should I use?**
- DeepSeek (default): General purpose
- OpenAI: Best for Python/ML
- Anthropic: Strong in several coding tasks

## Usage

**Q: How do I generate basic code?**
```python
from dscoder import AIAgent
agent = AIAgent()
code = agent.generate_code("Calculate mean and std dev")
```

**Q: Where is my generated code saved?**
```
output/
├── code_success_*.py  # Working code
├── code_failure_*.py  # Failed attempts
└── logs/              # Debug info
```

**Q: How do I debug failures?**
```python
agent = AIAgent(trace=True)
agent.metrics_collector.display_metrics()
```

**Q: Can I specify the programming language?**
```python
# Available: python, r, julia, cpp, rcpp
code = agent.generate_code(
    description="Sort array",
    language="python"
)
```

## Common Issues

**Q: Code generation fails?**
- Check API keys
- Increase timeout: `agent = AIAgent(timeout=180)`
- Enable tracing: `trace=True`
- Check logs in `output/logs/`

**Q: How do I handle timeouts?**
```python
agent = AIAgent(
    timeout=180,
    max_attempts=10
)
```

**Q: Provider not responding?**
```python
# Switch providers
agent.llm_client.switch_provider("openai")
```

## Features

**Q: What languages are supported?**
- Python (`python`): Data science/ML
- R/Rcpp (`r`): Statistics
- Julia (`julia`): Numerical computing
- C++ (`cpp`): Performance computing

**Q: Can I validate outputs?**
```python
code = agent.generate_code(
    description="Sort [5,1,3]",
    expected_output="[1,3,5]"
)
```

**Q: How do I monitor usage?**
```python
agent.metrics_collector.display_metrics()
```

## Examples

**Q: How do I generate ML code?**
```python
code = agent.generate_code("""
1. Load iris dataset
2. Train RandomForest
3. Print accuracy
""")
```

**Q: Statistical analysis in R?**
```python
code = agent.generate_code(
    """
    1. Load mtcars
    2. Run ANOVA
    3. Plot results
    """,
    language="r"
)
```

**Q: Numerical computing in Julia?**
```python
code = agent.generate_code(
    "Implement gradient descent",
    language="julia"
)
```

## Support

**Q: Where do I get help?**
- Issues: github.com/evandeilton/dscoder/issues
- Docs: github.com/evandeilton/dscoder/docs
- API Docs:
  - DeepSeek: platform.deepseek.com/docs
  - OpenAI: platform.openai.com/docs
  - Anthropic: docs.anthropic.com/claude -->