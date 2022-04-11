from requests import get
from bs4 import BeautifulSoup

#function to scrap the book website
#This function returns the informations regarding the book.

def web_scrapping(url):
    page = get(url)
    product_info = {}
    product_info_title = []
    product_info_value = []

    #use of BeautifulSoup to parse the Html web page of the book
    soup = BeautifulSoup(page.content, 'html.parser')

    # Get the title book
    product_info_bs = soup.find_all("h1")
    product_info['title'] = product_info_bs[0].string

    # Get the description book
    product_info_bs = soup.find_all("p")
    product_info['Description'] = product_info_bs[3].string
    if product_info['Description'] != None :
        product_info['Description'] = product_info['Description'].encode('utf-8', 'ignore')
        product_info['Description'] = product_info['Description'].decode('ASCII', 'ignore')

    # Get the category book
    product_info_bs = soup.find_all("a")
    product_info['category'] = product_info_bs[3].string

    #Get the UPC, price with tax, price without tax, the availability, the number of reviews
    product_info_bs = soup.find_all("td")
    for Pr_info in product_info_bs:
        product_info_value.append(Pr_info.string)
    product_info_bs = soup.find_all("th")
    for Pr_info in product_info_bs:
        product_info_title.append(Pr_info.string)

    for i in range(0, len(product_info_title)):
        product_info[product_info_title[i]] = product_info_value[i]


    return [url, product_info['UPC'], product_info['title'], product_info['Price (incl. tax)'], product_info['Price (excl. tax)'], product_info['Availability'], product_info['Description'], product_info['category'], product_info['Number of reviews']]

def get_Link(soup_ex):
    link = soup_ex.find_all('li', class_='next')[0]
    link_2 = str(link.find_all('a')[0].get('href'))
    return link, link_2