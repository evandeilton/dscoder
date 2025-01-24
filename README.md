# dscoder - AI Code Generation for Data Science

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

[Canal Argonalyst](https://www.youtube.com/watch?v=hTc_uDx0zVI)
















<!-- # dscoder - AI Code Generation for Data Science



[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) [![Python](https://img.shields.io/badge/python-3.8%2B-blue)]() [![Coverage](https://coveralls.io/repos/github/evandeilton/dscoder/badge.svg)]()

**dscoder** is an advanced AI-powered code generation system tailored for data science and statistical computing. It supports multiple programming languages, including Python, R, Julia, C++, and Rcpp, enabling seamless integration into your data workflows.

![dscoder in action](assets/peek-dscoder-ex-01.gif)

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Jupyter Notebook](#jupyter-notebook-usage)
  - [Terminal](#terminal-usage)
- [Common Patterns](#common-patterns)
  - [Data Science Pipeline](#data-science-pipeline)
  - [Statistical Analysis](#statistical-analysis)
- [FAQ](#faq)
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

### API Key Setup and Models

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

**Q: Where do I get model names to use?**

- **DeepSeek**: `deepseek-chat` (default) and `deepseek-reasoner` (more expensive)

For OpenAi and Anthropic unless you don't want ro read API documentation, you need first of all set the Keys and after that find out model names by command line.

- **OpenAI**: you can list models by using in terminal

```bash
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```

- **Anthropic**: Same way as OpenAi

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
# Available languages: python, r, julia, cpp
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

# Acknowledgement

[Canal Argonalyst](https://www.youtube.com/watch?v=hTc_uDx0zVI) -->
