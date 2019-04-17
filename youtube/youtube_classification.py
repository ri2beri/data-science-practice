import requests
from bs4 import BeautifulSoup
starting_url = "https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ"
r = requests.get(starting_url)
print(r.text)

soup = BeautifulSoup(r.text)
video_title_class = "yt-simple-endpoint style-scope ytd-grid-video-renderer"

print(soup.find_all("a", class_ = video_title_class ))



