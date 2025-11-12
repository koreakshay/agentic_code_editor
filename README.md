<h1 align="center">🤖 AI Coding Agent</h1>
<p align="center"><strong>Secure, Context-Aware Function Calling Assistant using Google Gemini</strong></p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue" alt="Python version" />
  <img src="https://img.shields.io/badge/Google%20Gemini-API-green" alt="Gemini API" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License: MIT" />
  <img src="https://img.shields.io/badge/Built%20with-%E2%9D%A4%EF%B8%8F%20in%20Python-red" alt="Built with love" />
</p>

---

## Project Overview
Built a toy version of Claude Code or Cursor's Agentic Mode using Google's free Gemini API
The project demonstrates:
- Integration of **LLM reasoning** with **secure local function execution**
- Use of **structured function schemas** (`types.FunctionDeclaration`) and **tool orchestration**
- Contextual multi-turn conversation handling for step-by-step reasoning

## Features
- Interact with Google Gemini AI models.
- Execute commands and manage files in natural language.
- Secure sandboxed working directory to prevent unauthorized access.
- Verbose output for detailed debugging and tracking.
- Simple setup and usage with Python and uv runtime.

## Installation

### Prerequisites
- Python 3.8 or higher
- `uv` runtime (can be installed via `pip install uv`)

### Steps
1. Clone the repository:
   ```
   git clone https://github.com/koreakshay/agentic_code_editor.git
   cd agentic_code_editor
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. (Optional) Install `uv` runtime globally:
   ```
   pip install uv
   ```

## Usage

Run the main script with a command prompt to interact with the AI Agent:

```bash
uv run main.py "get files"
```

- Replace `"get files"` with any command you want the AI to process.
- Use the `--verbose` flag to get detailed output for debugging:

```bash
uv run main.py "get files" --verbose
```

Verbose mode provides step-by-step logs of the AI interactions and command executions.

## Project Structure

- `main.py`: The entry point of the application. Handles command-line arguments, sets up the AI environment, and manages the workflow.
- `functions/`: Contains reusable function definitions used by the AI to perform tasks.
- `agent.py`: Manages the AI agent's logic and interaction with the Google Gemini SDK.
- `requirements.txt`: Lists Python dependencies.
- `.env`: Environment variables and API keys (not included in the repo for security).

## Technology Stack

- **Google Gemini SDK**: For AI model interaction.
- **Python**: Core programming language.
- **dotenv**: For managing environment variables securely.
- **uv**: A runtime for running Python scripts with enhanced features.

## Security Notes

The AI Agent operates within a sandboxed working directory to ensure that all file operations are contained and do not affect the user's broader file system. This approach mitigates risks associated with executing AI-generated commands.

## Future Enhancements

- Integration with additional AI models and APIs.
- Enhanced natural language understanding for more complex commands.
- Giving it more functions to call
