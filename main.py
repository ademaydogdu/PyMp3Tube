from __future__ import unicode_literals
import re
from bs4 import BeautifulSoup
import youtube_dl
import sys
import time
from selenium import webdriver
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import os
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import platform





url = "https://www.youtube.com/results?search_query="
kw = []
#kw.append(input("Şarkı ya da şarkıcı adını giriniz ... : ").split(','))
kw = list(map(str, input("Please give keyword.Example: Michael Jackson ... : ").split(',')))


if len (kw) == 0:
    print ("Not Empty . . . ")

elif len (kw) == 1:    
     kw0 = "".join(kw[0])
     gurl = url + kw0
     print(gurl)

elif len (kw) == 2:
       kw0 = "".join(kw[0])
       kw1 = "".join(kw[1])
       print(kw[0])
       gurl = url + kw0.replace("'","") + '+' + kw1.replace("'","")
        
elif len (kw) == 3:
        kw0 = "".join(kw[0])
        kw1 = "".join(kw[1])
        kw2 = "".join(kw[2])
        gurl = url + kw0.replace("'","") + '+' + kw1.replace("'","") + '+' + kw2.replace("'","")
        



driver = webdriver.Chrome(executable_path=r"C:\Users\root\AppData\Local\Programs\Python\Python38\Scripts\chromedriver.exe") # Edit path chromedriver.exe
driver.get(gurl)
while(True):
    height = driver.execute_script("return document.body.scrollHeight")
    time.sleep(1)
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    if int(height)==0:
        break

time.sleep(4)



with open('sources.txt','w',encoding="utf-8") as z:
    z.write(driver.page_source)

listLink = []
listTitle = [] 
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

aTitles = []
aLinks = []
source = open('sources.txt','r',encoding="utf-8")
soup = BeautifulSoup(source,'html.parser')

#source = soup.findAll('a', {'class': 'yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link'})
titles = soup.findAll('yt-formatted-string', {'class': 'style-scope ytd-video-renderer'})


    
    


lnks = open('results.txt','w')

regex = r"(/watch?v=...........)"

urls = []

for a in soup.findAll('a',{'id': 'video-title'}):
    with open('results.txt','w') as z:
        for b in soup.findAll('a',href=True):
            z.writelines(str(b['href']) + '\n')

regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"



c = open('results.txt','r')
myresult = [row.split(',') for row in c.readlines()]

j = 0

for index in range(len(myresult)):
    for i in myresult[index]:
        if len(i) == 21 and 'watch' in i:
             urls.append(i)
             
urls = list(dict.fromkeys(urls))           
              
    
for title in titles:
    aTitles.append(title.text)
    

del aTitles[1::2]    
for t,u in zip(aTitles,urls):
        print(aTitles.index(t) + 1,end=' ' + '\t\t' )
        print(" " + t + '\t\t' + u)




choice = int(input("İndirilmesini istediğiniz şarkının numarasını giriniz.."))
choice = choice - 1

def dchoice(choice):
    a = urls[choice].replace("'","")
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['http://www.youtube.com' + a])
dchoice(choice)    
    
    
time.sleep(4)    

if os.path.isfile('./results.txt'):
	os.remove("results.txt")

else:
	pass    
