import requests
from bs4 import BeautifulSoup
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
