"""Lesson task """
import requests
from bs4 import BeautifulSoup

def find_link_depth(url, target_page, depth):
    """ Function that tests the theory of n handshakes, only for wikipedia """
    if depth == 0:
        return False
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        for link in links:
            next_url = link['href']
            print(next_url)
            if "/wiki/" in next_url and "http" not in next_url:
                next_page = "https://ru.wikipedia.org" + next_url
                if next_page == target_page:
                    print(f"Достигнута целевая страница: {target_page}")
                    return True
                find_link_depth(next_page, target_page, depth - 1)
    except KeyError:
        pass
    return False

print(find_link_depth("https://ru.wikipedia.org/wiki/Python",
                       "https://ru.wikipedia.org/wiki/Cython",
                         2))
