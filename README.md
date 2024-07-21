# Myntra-Hackerramp-Disability-Inclusion-Feature
This Disability-Inclusion-Feature is designed to create a more inclusive shopping environment by providing tools for visually impaired and upper limb disabled individuals. The assistant uses advanced text-to-speech (TTS) and speech-to-text (STT) technologies to make shopping more accessible and user-friendly.

Features
Text-to-Speech Model
Product Descriptions: Reads out product descriptions, prices, and reviews for blind or low vision users.
User Engagement: Boosts confidence and engagement by making product information easily accessible.
Libraries Used:
gtts (Google Text to Speech)
Selenium for web scraping
BeautifulSoup for parsing HTML
Workflow:
Input: The model scrapes the required data from the website.
Output: The model converts the text into speech, generates an audio file (.mp3), and plays it.
Voice Command Integration
Hands-Free Navigation: Allows users to navigate the app and make purchases using voice commands.
User-Friendly: Enhances the overall user experience by providing an intuitive, hands-free interface.
Libraries Used:
speechRecognition
pyaudio
webbrowser
os
re
ChromeDriver for web automation
Selenium and BeautifulSoup for web scraping
Workflow:
Input: The model recognizes the user's voice as input.
Output: The model searches for the product on the Myntra website and opens the page in the web browser.
Virtual Assistant
Guided Shopping: Guides users through the shopping process, listens to them, and helps them navigate through the app.
Seamless Interaction: Combines TTS and STT models to create a smooth and interactive shopping experience.
Inclusivity
Enhanced Accessibility: Creates a more inclusive environment, leading to higher satisfaction and increased usage.
Customer Loyalty: Strengthens customer loyalty by providing an accessible and enjoyable shopping experience.
Installation
To get started with the Disability-Inclusion-Feature, follow these steps:

Clone the repository:

sh
Copy code
git clone https://github.com/yourusername/disability-inclusion-feature.git
cd disability-inclusion-feature
Install the required dependencies:

sh
Copy code
pip install -r requirements.txt
Run the setup script to configure the environment:

sh
Copy code
python setup.py
Usage
Start the application:

sh
Copy code
python app.py
Follow the on-screen instructions to use the text-to-speech and speech-to-text features.

Use voice commands to navigate through the app and make purchases.

Contributing
We welcome contributions to the Disability-Inclusion-Feature! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

