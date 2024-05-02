import requests
from bs4 import BeautifulSoup

def get_vector_store_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Now you can parse the HTML and extract the relevant information
    # For example, you can extract the article title and text
    title = soup.find('h1', class_='graf--title').text
    text = soup.find_all('p')
    # Now you can do something with the title and text
    print(title)
    for p in text:
        print(p.text)