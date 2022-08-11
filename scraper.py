import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/The_Walking_Dead_(TV_series)"

def get_citations_needed_count(url): 
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    citations_needed_count = soup.find("span", {"id": "citations-needed-count"}).text
    return citations_needed_count

def get_citations_needed_list(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    citations_needed_list = soup.find("div", {"id": "citations-needed-list"}).text
    return citations_needed_list

get_citations_needed_count(url)
get_citations_needed_list(url)