from requests import get
from bs4 import BeautifulSoup
import csv
from function_web_scrapping import web_scrapping
import pandas as pd

#this function returns the list of books for one category in a CSV file

def category_web_scrap(url, category, url_home, link_index):
    i = 0
    books_List_Url = []
    page = get(url)
# use of BeautifulSoup to parse the Html web page of the catgeory
    soup = BeautifulSoup(page.content, 'html.parser')
    nb_list = int(soup.find_all("strong")[1].string)
#list of titles for the CSV file
    en_tete = ["product_page_url","UPC","title","price_including_tax","price_excluding_tax","number_available","product_description","category","review_rating"]
    if nb_list != 0:
#get the list of All book's url for the first page of the category
        for link in soup.find_all('h3'):
            link_2 = link.find_all('a', href=True)[0].get('href')
            link_2 = link_2.replace("../", "")
            books_List_Url.append(url_home + link_2)
# get the list of all book's url for the other pages of the category
        if nb_list > 21:
            for p in range(int(nb_list / 20)-1):
#go to the next page and parse the HTML next page
                link_page = soup.find_all('li', class_='next')[0]
                link_3 = str(link_page.find_all('a')[0].get('href'))
                url_2 = url.replace(link_index, link_3)
                page = get(url_2)
                soup = BeautifulSoup(page.content, 'html.parser')
#get the list of books'URL of the current page
                for link_4 in soup.find_all('h3'):
                    link_5 = link_4.find_all('a', href=True)[0].get('href')
                    link_5 = link_5.replace("../", "")
                    books_List_Url.append(url_home + link_5)
#Writing in CSV file the informations needed for all books of the category
        with open(category + '.csv', 'w', newline = '') as fichier_csv:
            writer = csv.writer(fichier_csv, delimiter=";")
            writer.writerow(en_tete)
            while i < len(books_List_Url)-1:
                writer.writerow(web_scrapping(books_List_Url[i]))
                i += 1


