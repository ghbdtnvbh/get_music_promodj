from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests
from random import randint
from time import sleep

ua = UserAgent()
user_agent = ua.random
links = []


# Забираем ссылки на скачивание с двух первых страниц
def get_links():
    for i in range(1, 3):
        url = f'https://promodj.com/mixes?page={i}'        
        r = requests.get(url=url)
        soup = BeautifulSoup(r.text, "lxml")
        download = soup.find_all(class_="player_standard_tool player_standard_tool__downloads")
        for i in download:
            url = i.get("href")
            links.append(url)
# скачиваем mp3
def get_mp3():
    for i in range(len(links)):
        delay = randint(33,66)
        sleep(delay)
        headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "User-Agent": user_agent
                }
        ids = links[i].split('/')[4]
        r = requests.get(url=links[i], headers=headers, stream=True)
        with open (f"/home/pi/radio/music/{ids}.mp3", "wb") as f:
            f.write(r.content)
        

def main():
    get_links()
    get_mp3()

if __name__ == '__main__':
    main()