from bs4 import BeautifulSoup
import requests


url = 'https://en.wikipedia.org/wiki/The_Walking_Dead_(TV_series)'


def get_citations_needed_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    list_results = soup.findAll("a", attrs={"title": "Wikipedia:Citation needed"})
    print("Citations needed: ", len(list_results))


def get_citations_needed_report(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    list_results = soup.findAll("a", attrs={"title": "Wikipedia:Citation needed"})
    for item in list_results:
        print(item.parent.parent.parent.text)


get_citations_needed_count(url)
get_citations_needed_report(url)