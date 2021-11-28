import requests
from bs4 import BeautifulSoup
import translators as ts

name = input("Adınızı daxil edin: ")
url = f"https://www.urbandictionary.com/define.php?term={name}"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
response = requests.get(url, headers=headers).text

def getDefinition(content):
    return BeautifulSoup(content,"html.parser").find(class_="meaning").text

meaning = getDefinition(response)
translatedMeaning = ts.google(meaning, from_language="en",to_language="az")

print(f"{name} sözünün mənası:\n{translatedMeaning}")