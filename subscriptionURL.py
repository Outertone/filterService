import requests
from bs4 import BeautifulSoup
import pyperclip

def getBeforeURL():
    with open('subscriptionURL.txt', 'r') as file:
       return file.read()

def setSubscriptionURL(url):
    with open('subscriptionURL.txt', 'w') as file:
        file.write(url)

def getSubscriptionURL():
    url = 'https://v2cross.com/1884.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    urlNodeText =  soup.select(".entry-content h5")[0].get_text()
    return  urlNodeText.split('：')[1]

def getServicesByURL(url):
    response = requests.get(url)
    print(response.text)
    pyperclip.copy(response.text)



# 打印网页内容
# print(response.text)