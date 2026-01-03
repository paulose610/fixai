# Calculator App

A simple command-line calculator application built with Python that evaluates basic arithmetic expressions.

## Features

*   **Basic Arithmetic Operations**: Supports addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
*   **Operator Precedence**: Correctly handles the order of operations (e.g., multiplication and division before addition and subtraction).
*   **Error Handling**: Provides informative error messages for invalid expressions or tokens.
*   **JSON Output**: Presents the expression and its result in a structured JSON format.

## How to Run

### Prerequisites

Make sure you have Python 3 installed on your system.

### Usage

To run the calculator, execute the `main.py` script from your terminal, passing the arithmetic expression as a string argument.

```bash
python main.py "your_expression_here"
```

**Examples:**

1.  **Addition:**
    ```bash
    python main.py "5 + 3"
    ```
    Output:
    ```json
    {
        "expression": "5 + 3",
        "result": 8.0
    }
    ```

2.  **Multiplication and Addition (Precedence):**
    ```bash
    python main.py "3 + 5 * 2"
    ```
    Output:
    ```json
    {
        "expression": "3 + 5 * 2",
        "result": 13.0
    }
    ```

3.  **Division:**
    ```bash
    python main.py "10 / 2"
    ```
    Output:
    ```json
    {
        "expression": "10 / 2",
        "result": 5.0
    }
    ```

4.  **Invalid Expression:**
    ```bash
    python main.py "5 + "
    ```
    Output:
    ```
    Error: not enough operands for operator +
    ```

5.  **Invalid Token:**
    ```bash
    python main.py "5 & 3"
    ```
    Output:
    ```
    Error: invalid token: &
    ```

## Code Structure

*   **`main.py`**: The entry point of the application. It parses command-line arguments, initializes the `Calculator`, evaluates the expression, and prints the result.
*   **`pkg/calculator.py`**: Contains the `Calculator` class, which implements the core logic for parsing and evaluating arithmetic expressions using an infix evaluation algorithm with support for operator precedence.
*   **`pkg/render.py`**: (Implicitly gathered from `main.py`) Handles the formatting of the output, specifically to JSON.
*   **`tests.py`**: (If present) Contains unit tests for the calculator logic.

## How it Works (Briefly)

The `Calculator` class in `pkg/calculator.py` uses two stacks: one for values (numbers) and one for operators. It processes the expression token by token, applying operators based on their precedence. This approach allows for correct evaluation of complex arithmetic expressions without needing to convert to postfix (RPN) notation explicitly.
