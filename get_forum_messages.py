import requests
from bs4 import BeautifulSoup
import time

URL = "https://bitcointalk.org/index.php?action=profile;u=3;sa=showPosts;start="

with open("satoshi_forum.txt", "w", encoding='utf-8') as file:
    for i in range(1, 520, 20):
        time.sleep(1)
        print(i)
        response = requests.get(URL + str(i))
        
        if response.status_code == 200:
            source = response.text
            soup = BeautifulSoup(source, 'html.parser')

            for a in soup.find_all("tr", {'class': 'titlebg2'}):
                date_el = a.find_all("td")[2]
                date_text = date_el.text.strip()[4:]
                print(date_text)
                file.write(date_text + "\n")

        else:
            print(f"Failed to retrieve page {i}: Status code {response.status_code}")

