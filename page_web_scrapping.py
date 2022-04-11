from function_web_scrapping import web_scrapping

url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

product_page_url = web_scrapping(url)[0]
upc = web_scrapping(url)[1]
title = web_scrapping(url)[2]
price_including_tax = web_scrapping(url)[3]
price_excluding_tax = web_scrapping(url)[4]
number_available = web_scrapping(url)[5]
product_description = web_scrapping(url)[6]
category = web_scrapping(url)[7]
review_rating = web_scrapping(url)[8]
print(web_scrapping(url))
