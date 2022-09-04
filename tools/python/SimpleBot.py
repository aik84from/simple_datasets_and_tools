import requests
from bs4 import BeautifulSoup


class SimpleBot:
    def find_all(self, url, tag, attribute, headers, timeout):
        response = requests.get(url, headers=headers, timeout=timeout)
        soup = BeautifulSoup(response.content, 'html.parser')
        result = []
        for item in soup.find_all(tag):
            result.append([item.get(attribute), item.text])
        return result

