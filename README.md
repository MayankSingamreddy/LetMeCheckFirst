# LetMeCheckFirst

A lightweight prompt formatting tool that improves the accuracy of your AI coding queries. LetMeCheckFirst intercepts your prompts, refines them for clarity and precision, and then pastes the improved version right where you need it - perfect for developers who want to maximize the value of their AI coding assistants.

## Features

✨ **Start/stop recording** with Command+U  
🔄 **Process text** through local Ollama models  
⚡ **Instant pasting** of improved prompts  
🛠️ **Fully configurable** system prompt and model

## Requirements

- Python 3.6+
- Ollama running locally
- macOS with accessibility permissions

## Installation

1. Ensure Ollama is installed and running on your machine
2. Install the required Python packages:
   ```bash
   pip3 install pynput requests pyperclip
   ```
3. Grant accessibility permissions to Terminal.app or your Python IDE:
   - Go to **System Preferences** > **Security & Privacy** > **Privacy** > **Accessibility**
   - Add and enable your terminal application

## Usage

1. Run the script:
   ```bash
   python3 key_recorder.py
   ```
2. Press **Command+U** to start recording your prompt
3. Type your query or code question
4. Press **Command+U** again to stop recording
5. Place your cursor where you want the improved prompt
6. The formatted response will be automatically pasted

## Configuration

The script uses these default settings which you can modify:

- **Model**: Uses `phi4` by default (can be changed to any Ollama model)
- **System Prompt**: Customizable instruction for how prompts should be formatted
- **Ollama URL**: Default is `http://localhost:11434/api/generate`

## Troubleshooting

- If pasting doesn't work, ensure accessibility permissions are granted
- Check the `key_recorder.log` file for detailed error messages
- Make sure Ollama is running with your desired model available

## Exit

Press **Escape** to exit the application
