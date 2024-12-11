# ExplErr

A Python package that provides LLM-powered exception explanations.

Implemented using [APPL](https://github.com/appl-team/appl).

## Installation

```bash
pip install explerr
```

## Usage

### As a CLI tool

Instead of running your Python script with `python`, use `expython`:

```bash
expython your_script.py
```

### As a Python package

```python
from explerr import ExceptionWithExplanation

try:
    # Your code here
    result = 1 / 0
except Exception as e:
    raise ExceptionWithExplanation(e)
```
