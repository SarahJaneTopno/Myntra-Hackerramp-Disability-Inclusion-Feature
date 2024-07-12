import speech_recognition as sr
import webbrowser

sr.Microphone(device_index=1)

r = sr.Recognizer()
r.energy_threshold = 5000

with sr.Microphone() as source:
    print("Listening")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("{}".format(text))
        
        search_query = text.replace(" ", "-").lower()
        
        myntra_url = 'https://www.myntra.com/' + search_query
        webbrowser.open(myntra_url)
    except:
        print("Unrecognizable")
