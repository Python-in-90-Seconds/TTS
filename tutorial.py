# Text to Speech using Python's built-in features (no libraries)
print("🔊 Welcome to Python Text-to-Speech Demo!")

# Define a message to convert into speech
message = "Hello, I am your Python voice assistant!"

# Use built-in 'os' to call platform's speech engine
import os
os.system(f"say {message}")

# For Windows users, we can use 'SAPI.SpVoice' via COM interface
# Uncomment below lines if you're on Windows

# import win32com.client
# speaker = win32com.client.Dispatch("SAPI.SpVoice")
# speaker.Speak(message)

# For Linux users with 'espeak' installed
# Uncomment if you're on Linux

# os.system(f'espeak "{message}"')
