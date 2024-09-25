# voice-control-bot

This project implements a voice-controlled AI assistant that recognizes spoken commands using the speech_recognition library and captures audio input through sounddevice. The assistant can perform web searches on Wikipedia and open websites like YouTube and Google based on user commands. It utilizes macOS's text-to-speech feature to provide verbal feedback to the user. The assistant continuously listens for commands in a loop, allowing for ongoing interaction. Overall, it integrates speech recognition and web automation to enhance user experience through voice commands.

# If working on windows the install these:
```
pip install SpeechRecognition
pip install pywin32
pip install wikipedia-api
```
# If using macOS then insall these:
```
pip install SpeechRecognition
pip install wikipedia
pip install sounddevice

```
pywin32 Replacement: The win32com.client.Dispatch("SAPI.SpVoice") is replaced with the macOS command say via os.system().

And ya that it 👍
