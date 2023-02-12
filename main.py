import requests
from bs4 import BeautifulSoup
import csv
import pprint

url = "https://www.guru99.com/best-python-books.html"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,'
                  ' like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78'
}
# headers = {  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'  }
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')
page = soup.select('.lasso-box-1')
page_title = soup.find("h1", class_="entry-title").text.upper()
print(f'The list of "{page_title}" was saved to a file')

book_list = []
for book in page:
    title = book.find('a').text.strip().upper()
    rating = book.find('span').text.strip()
    a = book.find('p').text.strip("Author Name:")
    for book_link in book.find_all('a'):
        book_url = book_link.get('href')
    book_list.append((title, rating, a, book_url))

pprint.pprint(book_list)

with open("book_list.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Rating", "Author name", "url"])
    writer.writerows(book_list)
