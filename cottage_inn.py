#Get one webpage
# Load libraries for web scraping
from bs4 import BeautifulSoup
import requests
# Get a soup from a URL
url = 'https://cottageinn.com/pick-a-location/'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

#Get info from all tags of a certain type
# Get all tags of a certain type from the soup
# /html/body/div[2]/div/div/div[1]/div[3]/div/div[1]/div[2]/div[1]/div/a
tags = soup.find_all('h3')
# Collect info from the tags
collect_info = []
for tag in tags:
    # Get info from tag
    info = tag.text
    collect_info.append(info)

#Print the info
# Print the info
print(collect_info)