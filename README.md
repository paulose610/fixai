# FixAI - Coding Agent

FixAI is a CLI-based coding agent powered by Google's Gemini API. It can help you understand, debug, and modify code features within a specific project directory.

## Setup

1.  **Install dependencies** using `uv` (recommended):
    ```bash
    uv sync
    ```

2.  **Configure API Key**:
    Create a `.env` file and add your Gemini API key:
    ```env
    GEMINI_API_KEY=your_api_key_here
    ```

## Usage

Run the agent with a prompt using `uv run`:

```bash
uv run main.py "get directory info of the project root."
```

## How to Experiment

By default, the agent is configured to work on the `calculator/` folder in this repository. 

1.  **Try it out**: Ask the agent to explore or modify the calculator project.
    *   *“Explain the calculator code.”*
    *   *create a bug* then try to fix it via the agent
    *   *“Find and fix the bug in the project using an example”*

2.  **Work on your own project**:
    To point the agent to a different codebase, open `config.py` and change the `WORKING_DIR` variable:

    - Add the project directory into the repo.
    - Update the `WORKING_DIR` variable in `config.py` to point to the project directory.

    ```python
    # config.py
    WORKING_DIR = 'relative path tp your project'
    ```
3.  **Experiment with the prompt**:
    Modify `prompts.py` to change the agent's system instructions and behavior.

### Available Functions

The agent can use the following functions to interact with your codebase:
- `list_files`: List all files in a directory.
- `read_file`: Read the content of a specific file.
- `write_file`: Create or overwrite a file with new content.
- `search_code`: Search for a specific string or pattern across the project.
    
