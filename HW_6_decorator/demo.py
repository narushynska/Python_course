import sys

from load_texts import get_data_from_html, save_text__to_file
from key_words import get_top_words

reload(sys)
sys.setdefaultencoding('utf-8')

LINKS_FILE = 'links.txt'
AUTHOR = 'Ray Bredbery'
KEY_WORDS_FILE = 'author_most_using_words'

file_url = open(LINKS_FILE, 'r')
links = file_url.read().split('\n')

all_composition = AUTHOR


for link in links:
    name, text = get_data_from_html(link)
    save_text__to_file(name, text)
    all_composition += ('\n' + name + '\n\n' + text)
save_text__to_file(AUTHOR, all_composition)

top_words = get_top_words(all_composition)
save_text__to_file(KEY_WORDS_FILE, top_words)
