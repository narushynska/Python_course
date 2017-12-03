import urllib2
from bs4 import BeautifulSoup
from time import time

from utils import Logger
LOG_FILE = 'log.txt'

@Logger(LOG_FILE)
def get_data_from_html(link):
    start = time()
    page = urllib2.urlopen(link)
    soup = BeautifulSoup(page, 'html.parser')
    name = soup.find(attrs={'class': 'page_title'}).text
    text = soup.find(attrs={'id': 'storyText'}).text
    end = time()
    print 'Extract text from {url} in {diff} seconds'.format(diff=(end - start), url=link)
    return name, text

@Logger(LOG_FILE)
def save_text__to_file(name, text):
    start = time()
    file_text = open('data/' + name + '.txt', 'w')
    file_text.write(text)
    file_text.close()
    end = time()
    print 'Save into {path} -- {diff} seconds'.format(diff=(end - start), path='data/' + name + '.txt')
