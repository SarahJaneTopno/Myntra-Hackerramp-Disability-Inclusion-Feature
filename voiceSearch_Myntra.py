import speech_recognition as sr
import webbrowser
import os

sr.Microphone(device_index=1)

# Get the path to the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the HTML file
html_file = os.path.join(current_dir, 'mic.html')

# Open the HTML file in the default web browser
webbrowser.open(f'file://{html_file}')

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
