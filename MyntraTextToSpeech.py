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
link = "https://www.myntra.com/sweatshirts/the+souled+store/the-souled-store-checked-round-neck-acrylic-sweatshirt/26725732/buy"

driver.get(link)

html_content = driver.page_source

soup=BeautifulSoup(html_content,'html.parser')
items={}
items['The product is'] = soup.find('h1', attrs={'class':'pdp-title'}).text
items['name of the product is '] = soup.find('h1', attrs={'class':'pdp-name'}).text
items['price'] = soup.find('span', attrs={'class':'pdp-price'}).text
# target_div = soup.find('div', attrs={'class':'pdp-productDescriptorsContainer'})

product_description_container = soup.find('div', attrs={'class':'pdp-productDescriptorsContainer'})
product_description = product_description_container.find('p', attrs={'class':'pdp-product-description-content'}).text
items['product description '] = product_description
size_material = product_description_container.find_all('div',attrs={'class':'pdp-sizeFitDesc'})
material_care = ""
if(len(size_material)>=2):
    material_care = size_material[1].find('p',class_='pdp-sizeFitDescContent').text

else:
    material_care = size_material.find('p',class_='pdp-sizeFitDescContent').text
    
items['material and care '] = material_care

specification = product_description_container.find('div', attrs={'class':'index-sizeFitDesc'})
specs = specification.find_all('div', attrs={"class":'index-row'})
items['specifications']=""
for each in specs:
    title = each.find('div',attrs={'class':'index-rowKey'}).text
    cont = each.find('div',attrs={'class':'index-rowValue'}).text
    items['specifications']+= title + ", " + cont+"\n"
    
text=""
for k in items:
    text = text + "\n" + k + "\n " + items[k]

print(text)
#convert it to speech
tts = gTTS(text=text, lang='en')
tts.save("output.mp3")   
os.system("start output.mp3")





