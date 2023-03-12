import requests
import os
from bs4 import BeautifulSoup

# Website to be scraped   
url = "https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRE55YXpBU0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen"
r = requests.get(url)   #Requesting th eurl from the server 

#Getting html content and parsing it 
htmlcontent = r.content
soup = BeautifulSoup(htmlcontent,'html.parser')

#Storing the links and the text to store 
list = soup.find_all("h4",class_="gPFEn")
links = soup.find_all("a",class_="WwrzSb")

    
# Writing in the file of all the headlines and links to the headlines
with open("Headline.txt", "a", encoding="utf-8") as f:
    for (text,link) in zip(list,links):   #Itreating both list and set at the same time 
            addtext = str(text.string)
            k = link['href']
            k=k.replace(".","")   #Removing the additional dot in the link
            addlink = "https://news.google.com"+k
            f.write(addtext +' :- ' + addlink + '\n')   #Writing to the file and storing a data
        


