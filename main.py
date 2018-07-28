import requests
from bs4 import BeautifulSoup
from slackclient import SlackClient
from datetime import datetime
from slackclient import SlackClient
import time
import os

path = os.environ['bonjourPath']
slackToken = os.environ['slackToken']
counter = 0
temps = datetime.now()
today10h30am = temps.replace(hour=10, minute=30, second=0, microsecond=0)
today9h40am = temps.replace(hour=9, minute=40, second=0, microsecond=0)
fichierTime = fichier2 = open(path+'time.txt', 'a')
fichierTime.write("script exécuté le "+str(temps))
fichierTime.close()
while counter < 1 and today9h40am <= time < today10h30am:
    r = requests.get('http://dites.bonjourmadame.fr/')
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    timeStamp = soup.find(class_= 'post')
    image = timeStamp.findChildren('img')[0].get('src')
    fichier = open(path+'href.txt', 'r')
    old_image = fichier.read()
    fichier.close
    if old_image != image :
        fichier2 = open(path+'href.txt', 'w')
        fichier2.write(image)
        fichier2.close()
        print("prems")
        print(image)
        slack_token = slackToken
        sc = SlackClient(slack_token)
        sc.api_call(
        "chat.postMessage",
        channel="GBX2YBGN4",
        text="Preum's "+image,
        as_user=1
        )
        counter +=1
    else:
        time.sleep(60)
