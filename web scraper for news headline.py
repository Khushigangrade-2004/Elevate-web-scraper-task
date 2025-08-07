import requests
from bs4 import BeautifulSoup
import pandas as pd

#URL of the news website
url = "https://www.bbc.com/news"

#make an HTTP request
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#find headline elements - structure depends on the site
headlines = soup.find_all('h2') #BBC uses h2 for headlines

#Extract text from the elements
headline_list=[]
for h in headlines:
    text = h.get_text(strip=True)
    if text and text not in headline_list:
        headline_list.append(text)

#print headlines
print("Top News Headlines from BBC:")
for i ,headline in enumerate(headline_list[:10],1):
    print(f"{i}. {headline}")


with open("bbc_headlines.txt", "w", encoding="utf-8") as file:
    file.write("Top News Headlines from BBC:\n\n")
    for i, headline in enumerate(headline_list[:10], 1):  # Save top 10
        file.write(f"{i}. {headline}\n")

print("Headlines saved to bbc_headlines.txt ✅")                             
        
