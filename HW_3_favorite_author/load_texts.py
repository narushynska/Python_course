import urllib2
from bs4 import BeautifulSoup


def get_data_from_html(link):
    page = urllib2.urlopen(link)
    soup = BeautifulSoup(page, 'html.parser')
    name = soup.find(attrs={'class': 'page_title'}).text
    text = soup.find(attrs={'id': 'storyText'}).text
    return name, text


def save_text__to_file(name, text):
    file = open('data/' + name + '.txt', 'w')
    file.write(text)
    file.close()
