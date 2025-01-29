# DSCoder - Advanced AI-Powered Code Generation for Data Science

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) [![Python](https://img.shields.io/badge/python-3.8%2B-blue)]() [![Coverage](https://coveralls.io/repos/github/evandeilton/dscoder/badge.svg)]()

## Table of Contents

- [Introduction](#introduction)
- [Core Features](#core-features)
- [Installation and Setup](#installation-and-setup)
- [Quick Start](#quick-start)  <!-- Added Quick Start Section -->
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
| Python   | Data Science, ML | Package integration, Data processing | General data analysis |
| R/Rcpp   | Statistical Computing | Statistical analysis, High-performance computing | Statistical research |
| Julia    | Scientific Computing | Numerical computing, Optimization | Mathematical modeling |
| C++      | Performance Computing | STL optimization, Memory management | System-level operations |

### Provider Integration

| Provider   | Default Model | Alternative Models | Key Strengths |
|------------|---------------|-------------------|---------------|
| DeepSeek   | deepseek-chat | deepseek-reasoner | Cost-effective, Fast responses |
| OpenAI     | gpt-4        | gpt-4-turbo, o1-mini | Advanced understanding |
| Anthropic  | claude-3-5-sonnet-20241022 | claude-3-opus-20240229, claude-3-5-haiku-20241022 | Complex reasoning |

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

| Platform      | Configuration Method | Command |
|---------------|---------------------|---------|
| Linux/macOS   | Add to ~/.bashrc or ~/.zshrc | `export PROVIDER_API_KEY="your_key"` |
| Windows       | Set user environment variables | `setx PROVIDER_API_KEY "your_key"` |

Supported API keys. You can set up your favorite ones:
- DEEPSEEK_API_KEY
- OPENAI_API_KEY
- ANTHROPIC_API_KEY

## Quick Start  <!-- New Section -->
To quickly get started with DSCoder, follow these steps:

1. Clone the repository and install the dependencies as described in the Installation and Setup section.
2. Set up your API keys as environment variables.
3. Use the `dscoder()` function to generate code. For example:

```python
from dscoder import dscoder

code = dscoder(
    description="Create a function to calculate the mean of a list",
    language="python"
)
print(code)
```

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

| Parameter      | Type | Default | Description |
|----------------|------|---------|-------------|
| description    | str  | Required | Detailed requirements for code generation |
| language       | str  | "python" | Target programming language |
| provider       | str  | "deepseek" | LLM provider selection |
| model          | str  | None | Specific model to use |
| trace          | bool | False | Enable detailed logging |
| timeout        | int  | 120 | Global timeout in seconds |
| max_attempts   | int  | 5 | Maximum retry attempts |
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

| Aspect     | Guidelines | Example |
|------------|------------|---------|
| Clarity    | Be specific and detailed | "Implement a function that calculates moving averages with customizable window size" |
| Structure   | Break down complex requirements | "1. Input validation, 2. Computation, 3. Error handling" |
| Constraints | Specify limitations | "Must handle missing values and outliers" |
| Output     | Define expected results | "Return a DataFrame with original and averaged values" |

### Performance Optimization

| Category   | Technique | Description |
|------------|-----------|-------------|
| Token Usage| Precise prompts | Clear, concise descriptions |
| Runtime    | Parallel processing | Enable parallel execution when available |
| Memory     | Resource management | Optimize memory usage patterns |
| Caching    | Response caching | Store frequently used responses |

## Command Line Interface Usage

DSCoder provides a powerful command-line interface through its `main()` function, allowing you to generate code directly from your terminal. This section covers all available parameters and provides comprehensive examples for both Linux and Windows environments.

### Basic Command Structure

The basic structure for running DSCoder from the terminal is:

```bash
python -m dscoder "description" [optional parameters]
```

### Available Parameters

| Parameter      | Flag            | Type | Default | Description |
|----------------|------------------|------|---------|-------------|
| description    | (required)       | str  | N/A     | Code description (in quotes) |
| language       | --language       | str  | python  | Target programming language |
| provider       | --provider       | str  | deepseek| LLM provider to use |
| model          | --model          | str  | None    | Specific model to use |
| trace          | --trace          | flag | False   | Enable detailed logging |
| timeout        | --timeout        | int  | 120     | Global timeout in seconds |
| max_attempts   | --max_attempts   | int  | 5       | Maximum retry attempts |
| expected_output | --expected_output| str  | None    | Expected output for validation |

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
python -m dscoder "Create script for elegant statistical analysis that includes:
0. A gracefully planed analysis pipeline with tidyverse and tidymodels
1. Data preprocessing with outlier detection
2. Generation of publication-ready plots with ggplot2
3. Preprocess variables: One hot encoding for textual (eg. char and factor), scale for numeric variables
4. Training clasification model for creditability target (lightgbm, xgboost and Logistic regression)
5. Cross-validation and fine tuning parameters. train 0.7 and test 0.3
6. Add conditional check for missing packages/libraries, if some is missing, install before importing
7. Use scorecard::germancredit as data." \
    --language r \
    # --provider anthropic \
    # --model claude-3-opus-20240229 \
    --timeout 240 \
    --trace
```
- Data Science Complex Pipeline
```bash
python -m dscoder "Create a comprehensive statistical analysis pipeline:

0. Check required libraries: data manipulation, ML frameworks, visualization, stats. If missing, install.
1. Data import & validation: dimensions, types, missing values, quality, schema validation
2. Initial cleaning: duplicates, missing values, data types, inconsistencies, outliers
3. EDA: univariate, bivariate, target distribution, correlations, outliers, data drift
4. Feature processing: encoding (categorical), scaling (numeric), interactions, dimensionality reduction
5. Feature engineering: domain features, aggregations, selection, importance analysis
6. Split data: train (70%), test (30%), stratified CV folds, temporal validation if needed
7. Handle imbalance if target small class is <= 5%: distribution check, SMOTE/weights, validation
8. Setup models: baseline, Logistic, LightGBM, XGBoost, stacking/ensemble
9. Train & tune: CV optimization, early stopping, learning curves
10. Evaluate: ROC-AUC, precision-recall, confusion matrix, statistical tests
11. Interpret: importance, SHAP, PDP, error analysis, segment performance
12. Quality checks: model stability, residual analysis, bias detection

Use german credit data." \
   --language python \
   --timeout 240 \
   --max_attempts 3
```

- High-performance C++ implementation:
```bash
python -m dscoder "Implement a concurrent data structure that:
1. Provides thread-safe operations
2. Uses lock-free algorithms
3. Includes comprehensive benchmarking
4. Implements memory optimization
5. Handles error cases gracefully
6. You code mus be state of art. Fast for big data." \
    --language cpp \
    --provider openai \
    --model gpt-4o \
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

| Issue                  | Possible Cause         | Solution                      |
|-----------------------|------------------------|-------------------------------|
| Authentication Error   | Invalid API key        | Verify environment variables   |
| Generation Timeout     | Complex request        | Increase timeout parameter     |
| Validation Failure     | Output mismatch        | Check expected_output format   |
| Provider Error         | Service unavailable     | Switch to alternative provider |

### Error Messages

| Error Type              | Description            | Resolution                   |
|-------------------------|------------------------|-------------------------------|
| InvalidProviderError    | Unsupported provider    | Check provider parameter       |
| TimeoutError            | Execution timeout       | Increase timeout value         |
| ValidationError         | Output validation failed | Review expected output         |

### Best Practices for Terminal Usage

1. **Quote Management**:
   - Always enclose the description in quotes
   - Use single quotes for descriptions containing double quotes
   - For Windows CMD, use double quotes and escape inner quotes if needed

2. **Line Continuation**:
   - Linux/macOS: Use backslash (\)
   - Windows CMD: Use caret (^)
   - PowerShell: Use backtick (`)

3. **Parameter Organization**:
   - Group related parameters together
   - Place commonly changed parameters first
   - Use line continuations for better readability

4. **Error Handling**:
   - Enable tracing for detailed error information
   - Increase timeout for complex generations
   - Set appropriate max_attempts for reliability

## License and Credits

This project is licensed under the MIT License. See the LICENSE file for details.

Implementation inspired by [Canal Argonalyst](https://www.youtube.com/watch?v=hTc_uDx0zVI).

---

For additional support and updates, visit the project repository or submit issues through GitHub.
