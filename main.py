from fake_useragent import UserAgent
from clint.textui import progress
import requests
ua = UserAgent()
user_agent = ua.random
url = 'https://promodj.com/download/7553204/7553204.mp3'

headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
         "User-Agent": user_agent
         }
r = requests.get(url=url, headers=headers, stream=True)

with open("7553204.mp3", "wb") as file:
    total_length = int(r.headers.get('content-length'))
    for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
        if chunk:
            file.write(chunk)
            file.flush()