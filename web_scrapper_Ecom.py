import requests
from bs4 import BeautifulSoup
import pandas as pd
proxies = {
  "http": "https://async.scraperapi.com/jobs/1eb87e680528d114bfa71c75e278afca"
}
data={'title':[],'price':[]}
url="https://www.amazon.in/s?k=iphone&crid=F1PXCXZCV109&sprefix=iphone%2Caps%2C592&ref=nb_sb_noss_1"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"} 
r=requests.get(url,headers=headers)
soup=BeautifulSoup(r.content,'html.parser')
# print(soup)
spans=soup.select("span.a-size-medium.a-color-base.a-text-normal")
prices=soup.select("span.a-price")
for span in spans:
    print(span.string)
    data["title"].append(span.string)
for price in prices:
    if not("a-text-price" in price.get("class")):
        print(price.find("span").get_text())
        data["price"].append(price.find("span").get_text()) 
        if len(data["price"])==len(data["title"]):
            break

df=pd.DataFrame.from_dict(data)
df.to_csv("data.csv",index=False)