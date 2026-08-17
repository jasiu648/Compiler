# Compiler

A Python-based implementation of a compiler for the **CSoft** programming language — a simplified, C#-inspired language. This project demonstrates core compiler concepts including lexical analysis, syntax parsing, AST traversal, and LLVM-based code generation.

## Overview

CSoft is a statically/dynamically typed language supporting common programming constructs. The compiler takes CSoft source files as input and produces LLVM IR as output.

## Technology Stack

| Technology | Usage |
|------------|-------|
| **Python** (96.9%) | Core compiler implementation |
| **ANTLR** (2.7%) | Grammar definition and parser generation |
| **LLVM** (0.4%) | Backend code generation (IR output) |

## Features

- Supported types: `int`, `long`, `double`, `string`, `bool`
- Dynamic typing with optional explicit type declaration
- Standard I/O: `print()`, `read()`
- Arithmetic operators: `+`, `-`, `*`, `/`, `%`
- Single-line comments with `#`
- Lexical and syntax error reporting
- Integer and floating-point arrays
- Logical expressions: `AND`, `OR`, `XOR`, `NOT`
- Conditional statements: `if`
- Loop constructs: `repeat`, `while`
- Custom structures and classes
- User-defined functions

## Project Structure

```
Compiler/
├── README.md
├── .gitignore
├── src/                          # Source code
│   ├── main.py                   # Entry point
│   ├── CodeGenerator.py          # LLVM IR code generation
│   ├── ExtendedListener.py       # ANTLR parse tree listener
│   ├── utils.py                  # Utility functions
│   ├── grammar.g4                # CSoft grammar file
│   └── antlr_generated/          # ANTLR-generated parser/lexer files
│       ├── CSoftLexer.py
│       ├── CSoftParser.py
│       ├── CSoftListener.py
│       └── CSoftVisitor.py
└── tests/                        # Test files
    ├── test_files/               # CSoft source test programs
    │   ├── arithmetic_operations.txt
    │   ├── array_test.txt
    │   ├── bool_test.txt
    │   ├── class_test.txt
    │   ├── function_scope.txt
    │   ├── if_statement.txt
    │   ├── int_long_test.txt
    │   ├── loop_test.txt
    │   ├── read_test.txt
    │   ├── relation_test.txt
    │   └── structutre_test.txt
    └── test_llvm/                # Generated LLVM IR output
        └── result.ll
```

## Getting Started

### Requirements

- Python 3.8+
- [ANTLR4 Python runtime](https://pypi.org/project/antlr4-python3-runtime/)
- LLVM (for running generated IR)

### Installation

```bash
git clone https://github.com/jasiu648/Compiler.git
cd Compiler
pip install antlr4-python3-runtime
```

### Usage

Run the compiler on a CSoft source file:

```bash
cd src
python main.py ../tests/test_files/arithmetic_operations.txt
```

The compiler generates LLVM IR output to `tests/test_llvm/result.ll`.

## Example

A simple CSoft program:

```csharp
# Declare and print a variable
int x = 10;
int y = 20;
print(x + y);
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add my feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

## License

This project is open source. See [LICENSE](LICENSE) for details.

## Author

**jasiu648** — *Initial work*
