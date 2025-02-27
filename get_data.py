import requests
from bs4 import BeautifulSoup
import re

query = "Artificial Intelligence"
url = "https://en.wikipedia.org/w/api.php?action=opensearch&search={query}&limit=5&format=json"
page_url = "https://en.wikipedia.org/wiki/{title}"
response = requests.get(url.format(query=query))
data = response.json()

for i in range(len(data[1])):
    print(data[1][i])
    page = requests.get(page_url.format(title=data[1][i])).content
    clean_page = BeautifulSoup(page, "html.parser").get_text()

    filename = re.sub(r"[^\w]", "", data[1][i])
    print("Writing to file ", filename)
    with open(f"{filename}.txt", "w", encoding="utf-8") as f:
        f.write(clean_page)