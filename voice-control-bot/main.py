import speech_recognition as sr
import win32com.client
import webbrowser
import wikipedia

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("recognizing..")
            query = r.recognize_google(audio, language="en-in")
            print(f"user said : {query}")
            return query
        except Exception as e:
            return "Some error occured"


if __name__ == '__main__':
    s = "hello i am ai bot. How can i help you"
    print(s)
    speaker.Speak(s)
    while True:
        print("Listening..")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://wikipedia.com"],
                 ["google", "https://google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speaker.Speak(f"opening {site[0]}")
                webbrowser.open(site[1])
        if 'search' in query:
            query = query.replace("search", "")
            search_url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&titles={query}&rvprop=content"
            speaker.Speak(f"searching for {query}")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speaker.Speak(results)

        # speaker.Speak(query)
