# AI Coding Agent in Python

An autonomous coding agent built in Python that inspects repositories, applies code patches, and runs local verification tests using tool-calling capabilities. Powered by OpenRouter and managed with `uv`.

## Features

- **Tool Execution:** Read file contents, list directories, write/overwrite files, and execute isolated Python scripts.
- **Autonomous Loop:** Multi-turn tool execution loop that plans, acts, and verifies code fixes.
- **OpenRouter Integration:** Uses standard OpenAI-compatible completions with support for free and frontier models.
- **Sandboxed Path Resolution:** Built-in safeguards to restrict file operations to the designated working directory.

## Prerequisites

- [uv](https://github.com/astral-sh/uv) (recommended) or Python 3.11+
- An [OpenRouter API Key](https://openrouter.ai/)

## Setup

1. Clone this repository:
   ```bash
   git clone <repo-url>
   cd ai-agent-python
   ```

2. Create a `.env` file in the root directory:
   ```env
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   ```

3. Install dependencies:
   ```bash
   uv sync
   ```

## Usage

Run the agent with a prompt describing the task or bug to fix:

```bash
uv run main.py "Fix the bug: 3 + 7 * 2 shouldn't be 20"
```

To inspect token counts and tool responses during execution, pass the `--verbose` flag:

```bash
uv run main.py --verbose "Inspect pkg/calculator.py and add power operator support"
```

## Available Tools

| Tool | Purpose |
| :--- | :--- |
| `get_files_info` | Lists files and directories within a specified path. |
| `get_file_content` | Reads and returns the complete text of a target file. |
| `write_file` | Writes or overwrites file content at the specified path. |
| `run_python_file` | Runs a Python script with optional arguments via subprocess. |

## Project Structure

```text
├── call_function.py      # Tool dispatch and registry
├── functions/            # Individual tool implementations (read, write, run)
├── main.py               # Main agent execution loop and CLI entrypoint
├── pkg/                  # Target codebase for testing and bug fixes
├── prompts.py            # System prompts and behavior instructions
├── pyproject.toml        # Project metadata and dependencies
└── README.md
```
