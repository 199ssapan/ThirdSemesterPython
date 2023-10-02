import requests
from bs4 import BeautifulSoup


# resp = requests.get("https://ru.wikipedia.org/wiki/Python")

# bsobj = BeautifulSoup(resp.text, "html.parser")

# refs = bsobj.find_all("a")
# for ref in refs:
#     try:
#         print(ref['href'])
#     except KeyError:
#         continue
    
def find_link_depth(url, target_page, depth):
    if depth == 0:
        return False
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        for link in links:
            next_url = link['href']
            print(next_url)
            if "/wiki/" in next_url:
                next_page = "https://ru.wikipedia.org" + next_url
                # print(next_page)
                if next_page == target_page:
                    print(f"Достигнута целевая страница: {target_page}")
                    return True
                elif find_link_depth(next_page, target_page, depth - 1):
                    return True
    except Exception:
        pass
    return False


print(find_link_depth("https://ru.wikipedia.org/wiki/Python", "https://ru.wikipedia.org/wiki/Cython", 2))