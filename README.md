# Keystroke Recorder and Query Formatter

This application captures keystrokes between Command+U key combinations and sends the recorded text to Ollama for processing. The formatted response is then automatically typed out.

## Features

- Start/stop recording with Command+U
- Automatically sends captured text to Ollama for processing
- Types out the formatted response automatically
- Configurable system prompt and model

## Requirements

- Python 3.6+
- pynput
- requests
- Ollama running locally

## Installation

1. Ensure Ollama is installed and running on your machine
2. Install the required Python packages:
   ```
   pip3 install pynput requests
   ```

## Usage

1. Run the script:
   ```
   python3 key_recorder.py
   ```
2. Press Command+U to start recording keystrokes
3. Type your query
4. Press Command+U again to stop recording
5. The application will send your text to Ollama for processing
6. Once processed, the formatted response will be automatically typed out

## Configuration

You can modify the following variables in the script:
- `ollama_url`: The URL endpoint for Ollama (default: http://localhost:11434/api/generate)
- `system_prompt`: The system prompt used for query formatting
- `model`: The Ollama model to use (default: "llama3")

## Troubleshooting

If you encounter issues, check the `key_recorder.log` file for error messages.

## Exit

Press Escape to exit the application.
