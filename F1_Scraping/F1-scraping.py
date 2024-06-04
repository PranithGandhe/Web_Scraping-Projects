import requests
from bs4 import BeautifulSoup

url = 'https://www.formula1.com/en/latest/all.html'
response = requests.get(url)
print("ok")

# Check if the request was successful
if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    headlines = soup.find_all('p')
    print(f"Number of headlines found: {len(headlines)}")
    for index, headline in enumerate(headlines):
        print(f"{index + 1}.{headline.get_text()}")
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")
