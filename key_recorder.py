#!/usr/bin/env python3
"""

Key Recorder and Ollama Interface

This script captures keystrokes between Command+U key combinations and
sends the recorded text to Ollama for processing. The formatted response
is then automatically typed out.

IMPORTANT: macOS requires accessibility permissions for this script to work properly.
Please go to System Preferences > Security & Privacy > Privacy > Accessibility
and add Terminal.app (or your Python IDE) to the list of allowed applications.
"""

import time
import json
import logging
import requests
import pyperclip
import os
import subprocess
from pynput import keyboard
from pynput.keyboard import Key, Controller

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='key_recorder.log',
    filemode='a'
)
logger = logging.getLogger(__name__)

class KeyRecorder:
    def __init__(self):
        self.recording = False
        self.recorded_keys = []
        self.keyboard_controller = Controller()
        self.cmd_pressed = False
        self.ollama_url = "http://localhost:11434/api/generate"
        self.system_prompt = """
        You are a helpful AI assistant. Your task is to reformat user queries 
        to be more clear, concise, and effective. Your output should be ONLY 
        the reformatted query, without any additional text or explanations.
        """
        self.model = "phi4"  # Default model, can be changed
        
        # Set up keyboard listener
        self.listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        )

    def start(self):
        """Start the keyboard listener"""
        logger.info("Starting key recorder. Press Cmd+U to start/stop recording.")
        print("Starting key recorder. Press Cmd+U to start/stop recording.")
        self.listener.start()
        self.listener.join()  # Keep the program running

    def on_press(self, key):
        """Handle key press events"""
        try:
            # Check if command key is pressed
            if key == Key.cmd:
                self.cmd_pressed = True
                return

            # Check if 'u' is pressed while command is held
            if self.cmd_pressed and hasattr(key, 'char') and key.char == 'u':
                self.toggle_recording()
                return

            # If recording, store the key
            if self.recording:
                self.record_key(key)
                
        except Exception as e:
            logger.error(f"Error in on_press: {e}")

    def on_release(self, key):
        """Handle key release events"""
        if key == Key.cmd:
            self.cmd_pressed = False

        # Stop listener with Esc key for debugging/testing
        if key == Key.esc:
            logger.info("Escape key pressed, stopping listener")
            return False

    def toggle_recording(self):
        """Toggle recording state"""
        if not self.recording:
            # Start recording
            self.recording = True
            self.recorded_keys = []
            logger.info("Recording started")
            print("Recording started...")
        else:
            # Stop recording and process
            self.recording = False
            logger.info("Recording stopped")
            print("Recording stopped, processing...")
            self.process_recorded_keys()

    def record_key(self, key):
        """Record a pressed key"""
        if key == Key.space:
            self.recorded_keys.append(' ')
        elif key == Key.enter:
            self.recorded_keys.append('\n')
        elif key == Key.tab:
            self.recorded_keys.append('\t')
        elif key == Key.backspace:
            if self.recorded_keys:  # Only remove if there are keys recorded
                self.recorded_keys.pop()
        elif hasattr(key, 'char') and key.char is not None:
            self.recorded_keys.append(key.char)

    def process_recorded_keys(self):
        """Process the recorded keys and send to Ollama"""
        if not self.recorded_keys:
            logger.info("No keys recorded")
            print("No keys recorded")
            return
            
        recorded_text = ''.join(self.recorded_keys)
        logger.info(f"Recorded text: {recorded_text}")
        print(f"Recorded text: {recorded_text}")
        
        print("Sending to Ollama for processing...")
        # Send to Ollama and get response
        formatted_text = self.send_to_ollama(recorded_text)
        
        if formatted_text:
            print(f"\nFormatted text from Ollama: \n{formatted_text}\n")
            print("Place your cursor where you want the text to be pasted...")
            # Give a brief moment to position cursor
            time.sleep(1)
            self.paste_text(formatted_text)
        else:
            print("Failed to get response from Ollama")

    def send_to_ollama(self, text):
        """Send text to Ollama API and return the response"""
        try:
            payload = {
                "model": self.model,
                "prompt": text,
                "system": self.system_prompt,
                "stream": False
            }
            
            logger.info(f"Sending to Ollama: {text}")
            response = requests.post(self.ollama_url, json=payload)
            
            if response.status_code == 200:
                result = response.json()
                formatted_text = result.get('response', '')
                logger.info(f"Ollama response: {formatted_text}")
                return formatted_text
            else:
                logger.error(f"Ollama API error: {response.status_code} - {response.text}")
                return None
                
        except Exception as e:
            logger.error(f"Error sending to Ollama: {e}")
            return None

    def paste_text(self, text):
        """Paste text at cursor position using AppleScript for better reliability on macOS"""
        try:
            # Save original clipboard content
            try:
                original_clipboard = pyperclip.paste()
            except Exception:
                original_clipboard = ""
                
            # Copy the formatted text to clipboard
            pyperclip.copy(text)
            logger.info("Text copied to clipboard")
            print("Text copied to clipboard, now pasting...")
            
            # Use AppleScript to paste more reliably on macOS
            # This requires accessibility permissions
            applescript = '''
            tell application "System Events"
                keystroke "v" using command down
            end tell
            '''
            
            try:
                # Try using AppleScript for macOS (much more reliable)
                result = subprocess.run(['osascript', '-e', applescript], check=True, 
                                      capture_output=True, text=True)
                paste_success = True
            except subprocess.CalledProcessError as e:
                logger.error(f"AppleScript paste failed: {e}")
                
                # Check for a specific error code that indicates permission issues
                if "not allowed to send keystrokes" in str(e.stderr):
                    print("\nPERMISSIONS ERROR: macOS requires accessibility permissions.")
                    print("Go to System Preferences > Security & Privacy > Privacy > Accessibility")
                    print("Add Terminal.app (or your Python IDE) to the list of allowed apps.\n")
                
                paste_success = False
            except Exception as e:
                logger.error(f"AppleScript paste failed: {e}")
                print(f"AppleScript paste failed: {e}")
                paste_success = False
                
            # Fallback to keyboard controller if AppleScript fails
            if not paste_success:
                try:
                    # Simulate Command+V to paste
                    self.keyboard_controller.press(Key.cmd)
                    self.keyboard_controller.press('v')
                    self.keyboard_controller.release('v')
                    self.keyboard_controller.release(Key.cmd)
                except Exception as e:
                    logger.error(f"Keyboard controller paste failed: {e}")
                    print("Paste failed. Here's the text you can copy manually:")
                    print(f"---\n{text}\n---")
                    return
                    
            time.sleep(0.5)  # Wait for paste to complete
            
            # Restore original clipboard content after a short delay
            time.sleep(0.5)
            pyperclip.copy(original_clipboard)
            
            logger.info("Finished pasting operation")
        except Exception as e:
            logger.error(f"Error in paste operation: {e}")
            print(f"Error in paste operation: {e}")
            print("\nHere's the output text you can manually paste:")
            print(f"---\n{text}\n---")


if __name__ == "__main__":
    recorder = KeyRecorder()
    recorder.start()
