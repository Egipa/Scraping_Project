import requests
from bs4 import BeautifulSoup

url = "https://www.guru99.com/best-python-books.html"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,'
                  ' like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78'
}
# headers = {  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'  }
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')
page = soup.select('.lasso-box-1')

for book in page:
    title = book.find('a').text.strip().upper()
    rating = book.find('span').text.strip()
    a = book.find('p').text.strip()
    for book_link in book.find_all('a'):
        book_url = book_link.get('href')

    print(f'Book title: {title}, Rating: {rating},\n {a}, \n For more details visit page: {book_url}')
