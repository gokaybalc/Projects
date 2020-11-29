import time
import speedtest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as UReq
driver=webdriver.Firefox(executable_path="D:\\driver\\firefox\\geckodriver.exe")

my_url="https://www.instagram.com/gokaybalc/following/?hl=en"
uClient=UReq(my_url)
page_html = uClient.read()

uClient.close()
page_soup = soup(page_html,"html.parser")


containers= page_soup.findAll("li",{"class":"wo9IH"})
print(len(containers))
#container=containers[0]
#print(soup.prettify(container))

#print(container.div.img["alt"])

"""price=container.findAll("div",{"class":"_1vC4OE _2rQ-NK"})

ratings=container.findAll("span",{"class":"_38sUEc"})

#print(price[0].text)
filename="products.csv"
f=open(filename,"w")

headers="Product_Name,Pricing,Ratings\n"

f.write(headers)

for container in containers:
    product_name=container.div.img["alt"]

    price_container = container.findAll("div",{"class":"_1vC4OE _2rQ-NK"})
    price = price_container[0].text.strip()

    rating_container = container.findAll("span",{"class":"_38sUEc"})
    rating=rating_container[0].text

    trim_price=''.join(price.split(","))
    
    

    print("product name: " + product_name)
    print("price: " + price)
    print("ratings: " + rating )"""

