# Super Simple Stock Market

This is a command line tool designed to simulate a simple stock market

# Getting Started

## Prerequisites

Python version 3.7.3

## Virtual Environment _(Optional)_
It might be worth running this in an isolated environment. <br> Create a virtual environment as necessary:

| Platform | Shell    | Specify Python Version for venv             | Command to activate virtual environment |
|----------|----------|---------------------------------------------|-----------------------------------------|
| Unix     | bash/zsh | ``` python3.7 -m venv path/to/your/venv```| $ source \<venv\>/bin/activate          |
| Windows  | cmd.exe  | ``` py -3.7 -m venv path/to/your/venv```  | C:\\> \<venv\>\Scripts\activate.bat     |

Or see the [pydoc](https://docs.python.org/3/library/venv.html) for more information
# Usage

## Running the Stock Market

### Unix

```sh
python sssm/main.py
```
### Windows
```sh
python sssm\main.py
```

## Running the Tests
```sh
python -m unittest discover
```

# Notes

Linting done with `pycodelint`:
``` $ pycodestyle {source_file_or_directory} ```
