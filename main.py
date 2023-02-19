from bs4 import BeautifulSoup
import requests

#URL to Scrape
url = requests.get("https://quotes.toscrape.com")

#Parses the HTML code
soup = BeautifulSoup(url.text, "html.parser")

#<span class = "text" itemprop="text"></span>
quotes = soup.findAll("span", attrs={"class":"text"})

#<small class="author" itemprop="author"></small>
authors = soup.findAll("small", attrs={"class":"author"})

for quote, author in zip(quotes,authors):
    print(quote.text)
    print(author.text)

