# Agentic Code Editor

## Project Overview
Built a toy version of Claude Code or Cursor using Google's free Gemini API

## Features
- Interact with Google Gemini AI models seamlessly.
- Execute commands and manage files via AI-driven instructions.
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
   git clone https://github.com/koreakshay/aiAgent.git
   cd aiAgent
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
- GUI interface for easier interaction.
- Advanced logging and monitoring features.
- Support for multi-user environments.

## Contribution Guidelines

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

Please ensure your code follows the existing style and includes appropriate tests.