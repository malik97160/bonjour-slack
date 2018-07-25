import requests
from bs4 import BeautifulSoup
from slackclient import SlackClient
from datetime import datetime

counter = 1
time = str(datetime.now())
print(time)
while counter < 1 :
    r = requests.get('http://dites.bonjourmadame.fr/')
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    timeStamp = soup.find(class_= 'timestamp')
    href = timeStamp.find('a').get('href')
    fichier = open('href.txt', 'r')
    old_href = fichier.read()
    fichier.close
    if old_href != href :
        fichier2 = open('href.txt', 'w')
        fichier2.write(href)
        fichier2.close()
        print("prems")
        counter +=1
