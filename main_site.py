from requests import get
from bs4 import BeautifulSoup
import category_web_scrapping as cws
import os

url= "http://books.toscrape.com/index.html"
url2 = "http://books.toscrape.com/catalogue/"

index_str = "index.html"
page = get(url)
soup = BeautifulSoup(page.content, 'html.parser')

liste_soup = soup.find_all('ul', class_="nav nav-list")
path = os.getcwd()
path = os.getcwd() + "/category_books"

os.mkdir(path)
os.chdir(path)
for link in liste_soup[0].find_all('li'):
    link_2 = str(link.find_all('a', href=True)[0].get('href'))
    link_3 = url.replace(index_str, link_2)
    categories = str(link.find_all('a', href=True)[0].string)
    categories = categories.replace(" ","")
    categories = categories.replace("\n", "")
    cws.category_web_scrap(link_3, categories, url2, index_str)