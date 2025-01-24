# DSCoder - Advanced AI-Powered Code Generation for Data Science

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) [![Python](https://img.shields.io/badge/python-3.8%2B-blue)]() [![Coverage](https://coveralls.io/repos/github/evandeilton/dscoder/badge.svg)]()

## Table of Contents

- [Introduction](#introduction)
- [Core Features](#core-features)
- [Installation and Setup](#installation-and-setup)
- [System Architecture](#system-architecture)
- [Function Reference](#function-reference)
- [Language Support](#language-support)
- [Provider Details](#provider-details)
- [Examples and Use Cases](#examples-and-use-cases)
- [Troubleshooting](#troubleshooting)
- [Best Practices](#best-practices)
- [License and Credits](#license-and-credits)

## Introduction

DSCoder is an advanced AI-powered code generation system specifically designed for data science and statistical computing applications. Through its core `dscoder()` function, it provides seamless access to multiple LLM providers and supports various programming languages, helping data scientists and researchers generate high-quality, production-ready code.

![dscoder in action](assets/peek-dscoder-ex-01.gif)

## Core Features

### Supported Programming Languages

| Language | Primary Use Cases | Key Features | Best For |
|----------|------------------|--------------|-----------|
| Python | Data Science, ML | Package integration, Data processing | General data analysis |
| R/Rcpp | Statistical Computing | Statistical analysis, High-performance computing | Statistical research |
| Julia | Scientific Computing | Numerical computing, Optimization | Mathematical modeling |
| C++ | Performance Computing | STL optimization, Memory management | System-level operations |

### Provider Integration

| Provider | Default Model | Alternative Models | Key Strengths |
|----------|---------------|-------------------|---------------|
| DeepSeek | deepseek-chat | deepseek-reasoner | Cost-effective, Fast responses |
| OpenAI | gpt-4 | gpt-4-turbo, o1-mini | Advanced understanding |
| Anthropic | claude-3-5-sonnet-20241022 | claude-3-opus-20240229, claude-3-5-haiku-20241022 | Complex reasoning |

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- Git
- Virtual environment tool (venv recommended)
- Access to LLM provider APIs

### Installation Steps

```bash
# Clone the repository
git clone https://github.com/evandeilton/dscoder.git

# Navigate to project directory
cd dscoder

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

### API Configuration (Not provided)

To configure API keys as environment variables:

| Platform | Configuration Method | Command |
|----------|---------------------|---------|
| Linux/macOS | Add to ~/.bashrc or ~/.zshrc | `export PROVIDER_API_KEY="your_key"` |
| Windows | Set user environment variables | `setx PROVIDER_API_KEY "your_key"` |

Supprted API keys. You can set up your favorite ones:
- DEEPSEEK_API_KEY
- OPENAI_API_KEY
- ANTHROPIC_API_KEY

## Function Reference

### The dscoder() Function

The primary interface for code generation is the `dscoder()` function:

```python
from dscoder import dscoder

code = dscoder(
    description="Your code description",
    language="python",
    provider="deepseek",
    model=None,
    trace=False,
    timeout=120,
    max_attempts=5,
    expected_output=None
)
```

#### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| description | str | Required | Detailed requirements for code generation |
| language | str | "python" | Target programming language |
| provider | str | "deepseek" | LLM provider selection |
| model | str | None | Specific model to use |
| trace | bool | False | Enable detailed logging |
| timeout | int | 120 | Global timeout in seconds |
| max_attempts | int | 5 | Maximum retry attempts |
| expected_output | str | None | Expected output for validation |

## Examples and Use Cases

### Data Science Examples

Data Processing Pipeline:
```python
code = dscoder(
    description="""
    Create a data processing pipeline that:
    1. Reads data from multiple CSV files
    2. Performs data cleaning and transformation
    3. Applies feature engineering
    4. Implements data validation checks
    5. Exports processed dataset
    """,
    language="python",
    provider="deepseek"
)
```

### Statistical Analysis Examples

Advanced Statistics in R:
```python
code = dscoder(
    description="""
    Develop an R script that:
    1. Performs comprehensive statistical analysis
    2. Implements hypothesis testing
    3. Generates visualization using ggplot2
    4. Calculates effect sizes and power
    5. Exports results to a report
    """,
    language="r",
    provider="anthropic",
    model="claude-3-opus-20240229"
)
```

### Scientific Computing Examples

Numerical Computing in Julia:
```python
code = dscoder(
    description="""
    Create a Julia module that:
    1. Implements differential equation solvers
    2. Provides error estimation
    3. Optimizes performance with parallel processing
    4. Generates solution visualizations
    5. Exports results to HDF5
    """,
    language="julia"
)
```

## Best Practices

### Effective Prompt Engineering

| Aspect | Guidelines | Example |
|--------|------------|---------|
| Clarity | Be specific and detailed | "Implement a function that calculates moving averages with customizable window size" |
| Structure | Break down complex requirements | "1. Input validation, 2. Computation, 3. Error handling" |
| Constraints | Specify limitations | "Must handle missing values and outliers" |
| Output | Define expected results | "Return a DataFrame with original and averaged values" |

### Performance Optimization

| Category | Technique | Description |
|----------|-----------|-------------|
| Token Usage | Precise prompts | Clear, concise descriptions |
| Runtime | Parallel processing | Enable parallel execution when available |
| Memory | Resource management | Optimize memory usage patterns |
| Caching | Response caching | Store frequently used responses |

## Command Line Interface Usage

DSCoder provides a powerful command-line interface through its `main()` function, allowing you to generate code directly from your terminal. This section covers all available parameters and provides comprehensive examples for both Linux and Windows environments.

### Basic Command Structure

The basic structure for running DSCoder from the terminal is:

```bash
python -m dscoder "description" [optional parameters]
```

### Available Parameters

| Parameter | Flag | Type | Default | Description |
|-----------|------|------|---------|-------------|
| description | (required) | str | N/A | Code description (in quotes) |
| language | --language | str | python | Target programming language |
| provider | --provider | str | deepseek | LLM provider to use |
| model | --model | str | None | Specific model to use |
| trace | --trace | flag | False | Enable detailed logging |
| timeout | --timeout | int | 120 | Global timeout in seconds |
| max_attempts | --max_attempts | int | 5 | Maximum retry attempts |
| expected_output | --expected_output | str | None | Expected output for validation |

### Terminal Examples

Let's explore various command combinations for different scenarios:

#### Basic Usage (Linux/macOS)

Generate Python code with default settings:
```bash
python -m dscoder "Create a function to calculate the mean and standard deviation of a list of numbers"
```

#### Language Selection (Linux/macOS)

Generate R code:
```bash
python -m dscoder "Implement a linear regression analysis function with diagnostic plots" \
    --language r
```

Generate C++ code:
```bash
python -m dscoder "Create a template-based sorting algorithm implementation" \
    --language cpp
```

Generate Julia code:
```bash
python -m dscoder "Implement a differential equation solver using Runge-Kutta method" \
    --language julia
```

#### Provider and Model Selection (Linux/macOS)

Using OpenAI with a specific model:
```bash
python -m dscoder "Build a neural network classifier" \
    --provider openai \
    --model gpt-4-turbo
```

Using Anthropic with an advanced model:
```bash
python -m dscoder "Create a data preprocessing pipeline" \
    --provider anthropic \
    --model claude-3-opus-20240229
```

Using DeepSeek with the reasoning model:
```bash
python -m dscoder "Implement a graph traversal algorithm" \
    --provider deepseek \
    --model deepseek-reasoner
```

#### Advanced Parameters (Linux/macOS)

Enable tracing and increase timeout:
```bash
python -m dscoder "Build a comprehensive data analysis framework" \
    --trace \
    --timeout 180
```

Set maximum attempts and expected output:
```bash
python -m dscoder "Create a function to sort a list in ascending order" \
    --max_attempts 8 \
    --expected_output "[1, 2, 3, 4, 5]"
```

#### Complex Examples (Linux/macOS)

Comprehensive statistical analysis in R:
```bash
python -m dscoder "Create an R script for statistical analysis that includes:
1. Data preprocessing with outlier detection
2. Normality tests and distribution analysis
3. ANOVA with post-hoc tests
4. Generation of publication-ready plots
5. Export results to a detailed report" \
    --language r \
    --provider anthropic \
    --model claude-3-opus-20240229 \
    --timeout 240 \
    --trace
```

High-performance C++ implementation:
```bash
python -m dscoder "Implement a concurrent data structure that:
1. Provides thread-safe operations
2. Uses lock-free algorithms
3. Includes comprehensive benchmarking
4. Implements memory optimization
5. Handles error cases gracefully" \
    --language cpp \
    --provider openai \
    --model gpt-4-turbo \
    --max_attempts 10 \
    --trace
```

#### Windows Command Prompt Examples

Basic usage in Windows:
```cmd
python -m dscoder "Create a function to calculate fibonacci sequence"
```

Complex parameters in Windows:
```cmd
python -m dscoder "Implement a machine learning pipeline" ^
    --language python ^
    --provider anthropic ^
    --model claude-3-opus-20240229 ^
    --timeout 180 ^
    --trace
```

#### PowerShell Examples

Basic usage in PowerShell:
```powershell
python -m dscoder "Create a function to calculate fibonacci sequence"
```

Complex parameters in PowerShell:
```powershell
python -m dscoder "Implement a machine learning pipeline" `
    --language python `
    --provider anthropic `
    --model claude-3-opus-20240229 `
    --timeout 180 `
    --trace
```

## Troubleshooting Guide

### Common Issues and Solutions

| Issue | Possible Cause | Solution |
|-------|---------------|----------|
| Authentication Error | Invalid API key | Verify environment variables |
| Generation Timeout | Complex request | Increase timeout parameter |
| Validation Failure | Output mismatch | Check expected_output format |
| Provider Error | Service unavailable | Switch to alternative provider |

### Error Messages

| Error Type | Description | Resolution |
|------------|-------------|------------|
| InvalidProviderError | Unsupported provider | Check provider parameter |
| TimeoutError | Execution timeout | Increase timeout value |
| ValidationError | Output validation failed | Review expected output |

### Best Practices for Terminal Usage

1. Quote Management:
   - Always enclose the description in quotes
   - Use single quotes for descriptions containing double quotes
   - For Windows CMD, use double quotes and escape inner quotes if needed

2. Line Continuation:
   - Linux/macOS: Use backslash (\)
   - Windows CMD: Use caret (^)
   - PowerShell: Use backtick (`)

3. Parameter Organization:
   - Group related parameters together
   - Place commonly changed parameters first
   - Use line continuations for better readability

4. Error Handling:
   - Enable tracing for detailed error information
   - Increase timeout for complex generations
   - Set appropriate max_attempts for reliability

## License and Credits

This project is licensed under the MIT License. See the LICENSE file for details.

Implementation inspired by [Canal Argonalyst](https://www.youtube.com/watch?v=hTc_uDx0zVI).

---

For additional support and updates, visit the project repository or submit issues through GitHub.


<!-- # dscoder - AI Code Generation for Data Science

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) [![Python](https://img.shields.io/badge/python-3.8%2B-blue)]() [![Coverage](https://coveralls.io/repos/github/evandeilton/dscoder/badge.svg)]()

**dscoder** is an advanced AI-powered code generation system tailored for data science and statistical computing. It supports multiple programming languages, including Python, R, Julia, C++, and Rcpp, enabling seamless integration into your data workflows.

![dscoder in action](assets/peek-dscoder-ex-01.gif)

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Jupyter Notebook](#jupyter-notebook)
  - [Terminal](#terminal)
- [Common Patterns](#common-patterns)
- [FAQ](#faq)
- [License](#license)
- [Acknowledgement](#acknowledgement)

## Features

- **Multi-Language Support**: Generate code in Python, R, Julia, C++, and Rcpp.
- **Versatile Integration**: Compatible with Jupyter Notebooks and terminal environments.
- **Multiple Providers**: Choose between DeepSeek (default), OpenAI, and Anthropic for code generation.
- **Advanced Capabilities**:
  - Output validation
  - Error handling
  - Metrics collection
  - Customizable timeouts and retry attempts
  - **Model Selection**: Specify and switch between different models for each provider.

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

### Jupyter Notebook

#### Basic Setup

Start by importing and initializing the `AIAgent`:

```python
# Import the AIAgent from dscoder
from dscoder import AIAgent

# Initialize with DeepSeek (default provider and model)
agent = AIAgent()
```

**Parameters:**

| Parameter          | Type             | Default                | Description                                                                 | Used In                   |
|--------------------|------------------|------------------------|-----------------------------------------------------------------------------|---------------------------|
| `description`      | `str`            | **Required**           | Description of the code to be generated.                                    | `generate_code()`, `main()` |
| `language`         | `str`            | `"python"`             | Programming language for the generated code (`"python"`, `"r"`, `"julia"`, `"cpp"`, `"rcpp"`). | `generate_code()`, `main()` |
| `provider`         | `str`            | `"deepseek"`           | AI provider to use (`"deepseek"`, `"openai"`, `"anthropic"`).              | `AIAgent`, `main()`       |
| `model`            | `str`            | `"deepseek-chat"`      | Specific model to use for the chosen AI provider. If not specified, defaults are used. | `main()` |
| `trace`            | `bool`           | `False`                | Enable detailed logging and tracing of operations.                          | `AIAgent`, `main()`       |
| `timeout`          | `int`            | `120`                  | Global timeout in seconds for code generation and execution.               | `generate_code()`, `main()` |
| `max_attempts`     | `int`            | `5`                    | Maximum number of attempts for code generation retries.                     | `main()`, `generate_code()` |
| `expected_output`  | `Optional[str]`  | `None`                 | Expected output to validate the generated code.                             | `generate_code()`, `main()` |

#### Generating Code with Various Parameters

**Generating Python Code for Data Analysis:**

```python
code = agent.generate_code(
    description="""
    Develop a Python function that:
    1. Loads a CSV file into a pandas DataFrame.
    2. Cleans the data by handling missing values and outliers.
    3. Computes descriptive statistics.
    4. Generates visualizations using seaborn and matplotlib.
    5. Saves the processed data and plots to specified directories.
    """,
    language="python",
    max_attempts=3
)
print(code)
```

**Generating R Code for Statistical Analysis:**

```python
code = agent.generate_code(
    description="""
    Create an R script that performs comprehensive statistical analysis:
    1. Loads and cleans the 'mtcars' dataset.
    2. Conducts normality tests on key variables.
    3. Performs ANOVA to assess the impact of different factors.
    4. Executes post-hoc tests based on ANOVA results.
    5. Visualizes the findings using ggplot2.
    """,
    language="r"
)
print(code)
```

**Generating Julia Code for Numerical Computing:**

```python
code = agent.generate_code(
    description="""
    Implement a Julia module that solves differential equations using the Runge-Kutta method:
    1. Defines the differential equations.
    2. Implements the Runge-Kutta solver with error estimation.
    3. Plots the solution trajectories.
    4. Saves the results to a CSV file.
    """,
    language="julia",
    max_attempts=8
)
print(code)
```

**Generating C++ Code for Data Structures:**

```python
code = agent.generate_code(
    description="""
    Develop a C++ implementation of a Red-Black Tree with the following functionalities:
    1. Insertion of nodes.
    2. Deletion of nodes.
    3. Balancing the tree after insertions and deletions.
    4. Searching for elements within the tree.
    5. In-order traversal to display the tree structure.
    """,
    language="cpp",
    expected_output="A fully functional Red-Black Tree class with all specified operations."
)
print(code)
```

### Terminal

#### Command-Line Interface

Generate code directly from the terminal using the provided CLI.

**Basic Usage:**

```bash
python -m dscoder "Create a function to calculate the correlation matrix for a given dataset."
```

**Specify Language:**

```bash
python -m dscoder "Implement a binary search tree with insertion, deletion, and traversal methods." --language cpp
```

**Enable Tracing for Detailed Logs:**

```bash
python -m dscoder "Perform statistical analysis on survey data." --trace
```

**Set AI Provider and Model:**

```bash
# Using Anthropic with a specific model
python -m dscoder "Build a neural network classifier for image recognition." --provider anthropic --model claude-3-5-sonnet-20241022

# Using OpenAI with a specific model
python -m dscoder "Develop a sorting algorithm." --provider openai --model gpt-4
```

**Customize Timeout and Retry Attempts:**

```bash
python -m dscoder "Develop a complex data pipeline for ETL processes." --timeout 180 --max_attempts 10
```

## Common Patterns

### Data Science Pipeline

Streamline your data science workflow with these steps:

```python
# 1. Data Loading
code = agent.generate_code("Load and preprocess CSV data for analysis.")

# 2. Feature Engineering
code = agent.generate_code("Create a feature engineering pipeline to transform raw data.")

# 3. Model Training
code = agent.generate_code("Train a machine learning model using cross-validation techniques.")

# 4. Evaluation
code = agent.generate_code("Generate and visualize model evaluation metrics.")
```

### Statistical Analysis

Conduct comprehensive statistical analyses:

```python
# 1. Descriptive Statistics
code = agent.generate_code(
    description="Calculate comprehensive descriptive statistics for the dataset.",
    language="r"
)

# 2. Hypothesis Testing
code = agent.generate_code(
    description="Perform t-tests and chi-square tests to evaluate data significance.",
    language="r"
)

# 3. Visualization
code = agent.generate_code(
    description="Create statistical visualizations to represent analysis results.",
    language="r"
)
```

## FAQ

### API Key Setup and Models

**Q: Where do I get API keys?**

- **DeepSeek**: [platform.deepseek.com/api-keys](https://platform.deepseek.com/api-keys)
- **OpenAI**: [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
- **Anthropic**: [console.anthropic.com/settings/keys](https://console.anthropic.com/settings/keys)

**Q: How do I set up API keys?**

To apply API keys on Linux and Windows:

**Linux (local user):**

```bash
# Add to ~/.bashrc or ~/.zshrc
echo 'export DEEPSEEK_API_KEY="your_key"' >> ~/.bashrc
echo 'export OPENAI_API_KEY="your_key"' >> ~/.bashrc
echo 'export ANTHROPIC_API_KEY="your_key"' >> ~/.bashrc

# Apply changes
source ~/.bashrc
```

**Windows (user environment variables):**

```powershell
# Command Prompt (run as user)
setx DEEPSEEK_API_KEY "your_key"
setx OPENAI_API_KEY "your_key"
setx ANTHROPIC_API_KEY "your_key"
```

**Verify Keys:**

```python
import os
print(os.getenv('DEEPSEEK_API_KEY'))
print(os.getenv('OPENAI_API_KEY'))
print(os.getenv('ANTHROPIC_API_KEY'))
```

**Q: Where do I get model names to use?**

- **DeepSeek**: `deepseek-chat` (default) and `deepseek-reasoner` (more advanced).
- **OpenAI**: List models via terminal:
  
  ```bash
  curl https://api.openai.com/v1/models \
    -H "Authorization: Bearer $OPENAI_API_KEY"
  ```

- **Anthropic**: List models via terminal:
  
  ```bash
  curl https://api.anthropic.com/v1/models \
       --header "x-api-key: $ANTHROPIC_API_KEY" \
       --header "anthropic-version: 2023-06-01"
  ```

### General Usage

**Q: How do I generate basic code?**

```python
from dscoder import AIAgent

agent = AIAgent()
code = agent.generate_code("Calculate mean and standard deviation of a dataset.")
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
# Available languages: python, r, julia, cpp
code = agent.generate_code(
    description="Sort an array of integers in ascending order.",
    language="python"
)
```

**Q: How do I specify a particular model to use?**

You can specify the `model` parameter in `main()` call to utilize a specific model provided by the AI provider. It's better in Linux or Windows terminal.

```bash
## Other OpenAi models.
python -m dscoder "Build a neural network classifier for image recognition." --provider openai --model gpt-4o
python -m dscoder "Build a neural network classifier for image recognition." --provider openai --model o1-mini # Beware! Expensive!

## Other Anthropic models.
python -m dscoder "Build a neural network classifier for image recognition." --provider anthropic --model claude-3-5-haiku-20241022
python -m dscoder "Build a neural network classifier for image recognition." --provider anthropic --model claude-3-opus-20240229

## DeepSeek Most intelligent model deepseek-reasoner
python -m dscoder "Build a neural network classifier for image recognition." --provider deepseek --model deepseek-reasoner #Beware! Expensive!
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

Configure timeout settings and maximum attempts and logs:

```python
agent = AIAgent(
    timeout=180,
    trace=True
)
```

**Q: Provider not responding?**

Switch to a different AI provider:

```python
# Switch to OpenAI
agent.llm_client.switch_provider("openai")
```

### Advanced Features

**Q: What languages are supported?**

- **Python (`python`)**: Ideal for data science and machine learning.
- **R/Rcpp (`r`)**: Perfect for statistical analysis.
- **Julia (`julia`)**: Suitable for numerical computing.
- **C++ (`cpp`)**: Best for performance-critical applications.

**Q: Can I validate outputs?**

Yes, specify the expected output to validate the generated code:

```python
code = agent.generate_code(
    description="Sort the list [5, 1, 3] in ascending order.",
    expected_output="[1, 3, 5]"
)
```

**Q: How do I monitor usage?**

Display collected metrics using:

```python
agent.metrics_collector.display_metrics()
```

### Model Selection

Each AI provider offers multiple models with varying capabilities. By default, **dscoder** uses the following models:

- **DeepSeek**: `deepseek-chat` (low cost)
- **OpenAI**: `gpt-4` (low cost)
- **Anthropic**: `claude-3-5-sonnet-20241022` (expensive)

**Example: Specifying a Different Model via CLI**

You can override the default model by specifying the `model` via the command-line interface.

```bash
python -m dscoder "Create a logistic regression model in R." --provider openai --model gpt-4o
```

## Examples

**Q: How do I generate ML code?**

```python
code = agent.generate_code("""
Develop a Python script that:
1. Loads the Iris dataset.
2. Splits the data into training and testing sets.
3. Trains a RandomForest classifier with cross-validation.
4. Evaluates the model's accuracy and displays a classification report.
5. Saves the trained model and evaluation metrics.
""")
print(code)
```

**Q: Statistical analysis in R?**

```python
code = agent.generate_code(
    """
    Create an R script that:
    1. Loads the mtcars dataset.
    2. Cleans the data by handling missing values.
    3. Performs ANOVA to assess the impact of different variables.
    4. Executes post-hoc tests based on ANOVA results.
    5. Visualizes the findings using ggplot2.
    """,
    language="r"
)
print(code)
```

**Q: Numerical computing in Julia?**

```python
code = agent.generate_code(
    """
    Implement a Julia module that:
    1. Defines a system of differential equations.
    2. Solves them using the Runge-Kutta method.
    3. Estimates errors in the solutions.
    4. Plots the solution trajectories.
    5. Saves the results to a CSV file.
    """,
    language="julia"
)
print(code)
```


## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgement

[Canal Argonalyst](https://www.youtube.com/watch?v=hTc_uDx0zVI) -->
