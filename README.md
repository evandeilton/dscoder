# dscoder Examples

## Jupyter Notebook Usage

### Basic Setup
```python
import sys
sys.path.append("path/to/dscoder")
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