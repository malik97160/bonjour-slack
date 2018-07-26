import requests
from bs4 import BeautifulSoup
from slackclient import SlackClient
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

counter = 0
time = datetime.now()
today10h30am = time.replace(hour=10, minute=30, second=0, microsecond=0)
today9h45am = time.replace(hour=9, minute=45, second=0, microsecond=0)
# and  today9h45am < time < today10h30am
while counter < 1:
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

        msg = MIMEText(image)

        me = 'malik.couchy@gmail.com'
        you = 'clikclik97160@hotmail.fr'
        msg['Subject'] = 'Test'
        msg['From'] = me
        msg['To'] = you

        # Send the message via our own SMTP server, but don't include the
        # envelope header.
        s = smtplib.SMTP('localhost')
        s.sendmail(me, [you], msg.as_string())
        s.quit()

        counter +=1
