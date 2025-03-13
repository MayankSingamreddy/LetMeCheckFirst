<div align="center">

# 🔍 LetMeCheckFirst

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Ollama](https://img.shields.io/badge/Powered%20by-Ollama-green)](https://github.com/ollama/ollama)

A lightweight prompt formatting tool that improves the accuracy of your AI coding queries.

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [System Prompt](#system-prompt)
- [Troubleshooting](#troubleshooting)
- [Exit](#exit)

## 📖 Overview

LetMeCheckFirst intercepts your prompts, refines them for clarity and precision, and then pastes the improved version right where you need it - perfect for developers who want to maximize the value of their AI coding assistants.

## ✨ Features

<table>
  <tr>
    <td>✨</td>
    <td><b>Start/stop recording</b> with Command+U</td>
  </tr>
  <tr>
    <td>🔄</td>
    <td><b>Process text</b> through local Ollama models</td>
  </tr>
  <tr>
    <td>⚡</td>
    <td><b>Instant pasting</b> of improved prompts</td>
  </tr>
  <tr>
    <td>🛠️</td>
    <td><b>Fully configurable</b> system prompt and model</td>
  </tr>
</table>

## 🔧 Requirements

- Python 3.6+
- Ollama running locally
- macOS with accessibility permissions

## 📥 Installation

1. Ensure Ollama is installed and running on your machine
2. Install the required Python packages:

   ```bash
   pip3 install pynput requests pyperclip
   ```

3. Grant accessibility permissions to Terminal.app or your Python IDE:
   - Go to **System Preferences** > **Security & Privacy** > **Privacy** > **Accessibility**
   - Add and enable your terminal application

## 🚀 Usage

1. Run the script:

   ```bash
   python3 key_recorder.py
   ```

2. Press **Command+U** to start recording your prompt
3. Type your query or code question
4. Press **Command+U** again to stop recording
5. Place your cursor where you want the improved prompt
6. The formatted response will be automatically pasted

## ⚙️ Configuration

The script uses these default settings which you can modify:

| Setting | Default | Description |
|---------|---------|-------------|
| **Model** | `phi4` | Can be changed to any Ollama model |
| **System Prompt** | See below | Customizable instructions for prompt formatting |
| **Ollama URL** | `http://localhost:11434/api/generate` | API endpoint for Ollama |

## 💬 System Prompt

LetMeCheckFirst uses an advanced system prompt specifically designed for coding use cases. The prompt instructs the model to:

1. **Clarify ambiguities** in your query (language, framework, environment)
2. **Identify the correct level of detail** needed (code snippets vs. explanations)
3. **Detect intent and constraints** (performance needs, compatibility requirements)
4. **Preempt common issues** (misconceptions, security risks)
5. **Optimize for technical precision** (include parameters, return types)
6. **Format for optimal processing** using a structured template:

   ```
   [Task] → What you want to achieve
   [Context] → Relevant background details
   [Constraints] → Language, performance, security requirements
   [Expected Output] → Desired level of detail
   ```

You can customize this prompt in the `key_recorder.py` file to better suit your specific needs.

## ❓ Troubleshooting

- If pasting doesn't work, ensure accessibility permissions are granted
- Check the `key_recorder.log` file for detailed error messages
- Make sure Ollama is running with your desired model available

## 🚪 Exit

Press **Escape** to exit the application

---

<div align="center">
Made with ❤️ for developers who value precision
</div>
