from requests import get
from bs4 import BeautifulSoup
import csv
import urllib.request as ur


list_Images =[]
list_Name_Images =[]
#list of forbidden characters
list_Chars_Forb = [">", "<", ":", "/", "\'", "?", "*", "!","#","'", '"']
url = "http://books.toscrape.com/"
str_index = "index.html"
str_catalogue = "catalogue/"
url_2 = url + str_index
page = get(url_2)
# use of BeautifulSoup to parse the Html home page
soup = BeautifulSoup(page.content, 'html.parser')
nb_list = int(soup.find_all("strong")[0].string)

# get the list of all Images names

for link in soup.find_all('div', class_="image_container"):
    url_3 =[]
    link_2 = link.find_all('a')[0]
    link_3 = link_2.find_all('img')[0].get('src')
    url_3.append(url + link_3)
    list_Images.append(url_3)
    list_Name_Images.append(link_2.find_all('img')[0].get('alt'))

# get the list of all Images URL
for p in range(int(nb_list / 20) - 1):
    link_page = soup.find_all('li', class_='next')[0]
    link_page_2 = link_page.find_all('a')[0]
    link_page_3 = link_page_2.get('href')
    if p == 0:
        url_3 = url + link_page_3
    else:
        url_3 = url + str_catalogue + link_page_3
    page = get(url_3)
    soup = BeautifulSoup(page.content, 'html.parser')

    for link in soup.find_all('div', class_="image_container"):
        url_4=[]
        link_4 = link.find_all('a')[0]
        link_5 = link_4.find_all('img')[0].get('src')
        url_4.append(url + link_5)
        url_4[0] = url_4[0].replace("../","")
        list_Images.append(url_4)
        list_Name_Images.append(link_4.find_all('img')[0].get('alt'))
i = 0
#Create the CSV file to store the images name and URL
with open('images.csv', 'w', newline = '') as fichier_csv:
    writer = csv.writer(fichier_csv)
    while i < len(list_Images):
        writer.writerow(list_Images[i])
        i += 1

i=0
#use of the method urlretrieve to download the images in the folder
while i < len(list_Images):
    for char in list_Chars_Forb:
        list_Name_Images[i] = list_Name_Images[i].replace(char, "")
        list_Name_Images[i] = list_Name_Images[i].replace(" ", "_")
    ur.urlretrieve(list_Images[i][0],list_Name_Images[i] + ".jpg")
    i += 1
