# voice-control-bot
If working on windows the install these:
`` `
pip install SpeechRecognition
pip install pywin32
pip install wikipedia-api

```
If using MACOS then insall these:
```
pip install SpeechRecognition
pip install wikipedia
```
pywin32 Replacement: The win32com.client.Dispatch("SAPI.SpVoice") is replaced with the macOS command say via os.system().
And ya that it 👍
