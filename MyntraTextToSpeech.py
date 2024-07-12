from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from gtts import gTTS
import os




o={}

PATH = "C:/Users/diya brahma/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"

# Set up the Selenium WebDriver
service = Service(executable_path=PATH)
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.myntra.com/ethnic-dresses/anayna/anayna-red-floral-ethnic-a-line-cotton-midi-ethnic-dress/21334304/buy")

html_content = driver.page_source

soup=BeautifulSoup(html_content,'html.parser')

target_div = soup.find('div', attrs={'class':'pdp-productDescriptorsContainer'})


texts=""
for t in target_div:
    original = t.text
    formatted = ""
    for c in original:
        
        if(c.isupper() or c=="\n"):
            formatted = formatted + "\n"  
        formatted += c   
    texts = texts+formatted+"   "




# take a dictionary
items = {}
items['The product is'] = soup.find('h1', attrs={'class':'pdp-title'}).text
items['name of the product is '] = soup.find('h1', attrs={'class':'pdp-name'}).text
items['price'] = soup.find('span', attrs={'class':'pdp-price'}).text
items['product description'] = texts



finaltext=""
for k in items:
    finaltext = finaltext+"\n"+ k+" "+ items[k]+"\n"
   

tts = gTTS(text=finaltext, lang='en')
tts.save("output.mp3")   
os.system("start output.mp3")
print(finaltext)




