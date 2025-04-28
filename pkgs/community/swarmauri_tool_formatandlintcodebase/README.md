![Swamauri Logo](https://res.cloudinary.com/dbjmpekvl/image/upload/v1730099724/Swarmauri-logo-lockup-2048x757_hww01w.png)

<p align="center">
    <a href="https://pypi.org/project/swarmauri_tool_formatandlintcodebase/">
        <img src="https://img.shields.io/pypi/dm/swarmauri_tool_formatandlintcodebase" alt="PyPI - Downloads"/></a>
    <a href="https://github.com/swarmauri/swarmauri-sdk/pkgs/pkgs/community/swarmauri_tool_formatandlintcodebase">
        <img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/swarmauri/swarmauri-sdk/pkgs/pkgs/community/swarmauri_tool_formatandlintcodebase&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false" alt="GitHub Hits"/></a>
    <a href="https://pypi.org/project/swarmauri/swarmauri_tool_formatandlintcodebase">
        <img src="https://img.shields.io/pypi/pyversions/swarmauri_tool_formatandlintcodebase" alt="PyPI - Python Version"/></a>
    <a href="https://pypi.org/project/swarmauri/swarmauri_tool_formatandlintcodebase">
        <img src="https://img.shields.io/pypi/l/swarmauri_tool_formatandlintcodebase" alt="PyPI - License"/></a>
    <br />
    <a href="https://pypi.org/project/swarmauri/swarmauri_tool_formatandlintcodebase">
        <img src="https://img.shields.io/pypi/v/swarmauri_tool_formatandlintcodebase?label=swarmauri_tool_formatandlintcodebase&color=green" alt="PyPI - swarmauri_tool_formatandlintcodebase"/></a>
</p>

---

# `swarmauri_tool_formatandlintcodebase`

## Purpose

This package implements a tool for automatically formatting and linting a codebase, ensuring consistency with coding standards.

## Description

The `swarmauri_tool_formatandlintcodebase` package provides functionality to format and lint your codebase, making it compliant with common coding standards like PEP 8. The tool can apply changes automatically or provide previews of what the changes would look like before applying them.

## Installation

To install the `swarmauri_tool_formatandlintcodebase` package, you can use [Poetry](https://python-poetry.org/) or [pip](https://pip.pypa.io/en/stable/).

### Using Poetry

1. Make sure you have Poetry installed. If not, you can install it using the command:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Navigate to your project directory and run:
   ```bash
   poetry add swarmauri_tool_formatandlintcodebase
   ```

3. This will install the package along with its dependencies.

### Using pip

1. You can install the package directly from PyPI:
   ```bash
   pip install swarmauri_tool_formatandlintcodebase
   ```

### Dependencies

The following dependencies are required for this package:

- `swarmauri_core`
- `swarmauri_base`
- `swarmauri_standard`
- `pydantic`
- `requests`

For development, you may also want to install the following packages:

- `flake8`
- `pytest`
- `pytest-asyncio`
- `pytest-xdist`
- `pytest-json-report`
- `python-dotenv`

## Usage

To use the `swarmauri_tool_formatandlintcodebase`, you will typically instantiate the `FormatAndLintCodebaseTool` class and call it with the specified parameters. Below is an example of how to use the tool:

```python
from swarmauri_tool_formatandlintcodebase import FormatAndLintCodebaseTool

# Create an instance of the tool
tool = FormatAndLintCodebaseTool()

# Define the directory of your codebase
codebase_directory = '/path/to/your/codebase'

# Call the tool to format and lint the codebase
results = tool(
    directory=codebase_directory,
    preview=True,  # Set to True to see a preview of changes
    formatter='black',  # Specify your preferred formatter
    linter='eslint'  # Specify your preferred linter
)

# Print the results
print(results)
```

### Parameters

- `directory`: The path to the codebase you want to format and lint.
- `preview`: A boolean flag to indicate whether you want to see a preview of changes (default is `False`).
- `formatter`: The name of the formatter you wish to use, such as 'black' (default is 'black').
- `linter`: The name of the linter you wish to use, such as 'eslint' (default is 'eslint').

### Logging

The tool uses Python's built-in logging module to log the process of formatting and linting. You can configure the logging level and format as per your requirements.

By following the installation and usage instructions outlined above, you can easily integrate the `swarmauri_tool_formatandlintcodebase` into your Python projects for a more consistent and clean codebase.