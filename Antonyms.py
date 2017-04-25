import requests
from bs4 import *

#Get user input first.
antonym=input("Welcome! Please enter a word to find its antonyms! ")
antonym1=antonym.lower()

data=requests.get("http://www.synonym.com/antonyms/" + antonym1)
soup=BeautifulSoup(data.text,"html.parser")

#I'm trying to find the tag with the listed antonyms in it.
#<ul class="antonyms">
#Get all antonyms using the find_all function. Store antonyms inside a file.
soup2=soup.find_all('ul',{'class':'antonyms'})

f=open('AntonymTXT.txt','a')

for i in soup2:
    antons=i.find_all('a')
    for anton in antons:
        f.write(anton.string+"\n")
f.close()
