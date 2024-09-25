import speech_recognition as sr
import webbrowser
import wikipedia
import os  # for macOS TTS

def speak(text):
    os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        audio = r.listen(source)
        try:
            print("Recognizing..")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            print("Sorry, I couldn't recognize your voice. Error:", e)
            return "Some error occurred"

if __name__ == '__main__':
    s = "Hello, I am an AI bot. How can I help you?"
    print(s)
    speak(s)

    while True:
        query = takeCommand()

        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://wikipedia.com"], ["google", "https://google.com"]]
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                speak(f"Opening {site[0]}")
                webbrowser.open(site[1])

        if 'search' in query.lower():
            query = query.replace("search", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results for that search term, please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("No page found for that search.")
            except Exception as e:
                print("Error occurred:", e)
                speak("Some error occurred while fetching the search results.")
