import speech_recognition as sr
import webbrowser
import re

# Initialize the recognizer
r = sr.Recognizer()
r.energy_threshold = 5000

# Predefined product links
product_links = {
    "hm boys 3 pack jeans": "https://www.myntra.com/jeans/h%26m/hm-boys-3-pack-comfort-skinny-fit-jeans/26313234/buy",
    "crop cotton denim jacket": "https://www.myntra.com/jackets/street+9/street-9-v-neck-sleeveless-crop-cotton-denim-jacket/25578232/buy"
    # Add more product names and links here
}

def normalize_text(text):
    """Normalize text by converting to lowercase and removing punctuation."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text

def listen_for_product():
    with sr.Microphone() as source:
        print("Listening for product name...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said: {}".format(text))
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        return None

def open_product_page(product_name):
    normalized_name = normalize_text(product_name)
    print(f"Normalized product name: '{normalized_name}'")  # Debug statement
    product_url = product_links.get(normalized_name)
    if product_url:
        webbrowser.open(product_url)
        print(f"Opening product page for: {normalized_name}")
    else:
        print(f"Product '{normalized_name}' not found.")

if __name__ == "__main__":
    product_name = listen_for_product()
    if product_name:
        open_product_page(product_name)
    else:
        print("No product name detected.")
