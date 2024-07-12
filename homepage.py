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

driver.get("https://www.myntra.com/kurtis")

html_content = driver.page_source

soup=BeautifulSoup(html_content,'html.parser')

ul_tag = soup.find('ul', attrs={'class' : 'results-base'})
li_tag = ul_tag.find_all('li', attrs={'class':'product-base'})


list_items=[]
text=""
for li in li_tag:
    product = li.find('h4', attrs={'class':'product-product'}).text
    text = text +"\n"+product

   

tts = gTTS(text=text, lang='en')
tts.save("output.mp3")   
os.system("start output.mp3")
print(text)




