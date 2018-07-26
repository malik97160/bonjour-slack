import requests
from bs4 import BeautifulSoup
from slackclient import SlackClient
from datetime import datetime

counter = 0
time = datetime.now()
today10h30am = time.replace(hour=10, minute=30, second=0, microsecond=0)
today9h45am = time.replace(hour=9, minute=45, second=0, microsecond=0)
while counter < 1 and  today9h45am < time < today10h30am:
    r = requests.get('http://dites.bonjourmadame.fr/')
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    timeStamp = soup.find(class_= 'post')
    href = timeStamp.find('a').get('href')
    fichier = open('href.txt', 'r')
    old_href = fichier.read()
    fichier.close
    if old_href != href :
        fichier2 = open('href.txt', 'w')
        fichier2.write(href)
        fichier2.close()
        print("prems")
        image = timeStamp.find('a').findChildren('img')[0].get('src')
        print(image)

        counter +=1
