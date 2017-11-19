import sys
from datetime import datetime

from load_texts import get_data_from_html, save_text__to_file
from key_words import get_top_words

reload(sys)
sys.setdefaultencoding('utf-8')

LINKS_FILE = 'links.txt'
OUTHOR = 'Ray Bredbery'
KEY_WORDS_FILE = 'author_most_using_words'

file = open(LINKS_FILE, 'r')
links = file.read().split('\n')

all_composition = OUTHOR

start = datetime.now()
for link in links:
    name, text = get_data_from_html(link)
    save_text__to_file(name, text)
    all_composition += ('\n' + name + '\n\n' + text)

end = datetime.now()

print 'All files were downloaded and saved in {diff} seconds'.format(diff=(end - start).seconds)
save_text__to_file(OUTHOR, all_composition)

start = datetime.now()
top_words = get_top_words(all_composition)
save_text__to_file(KEY_WORDS_FILE, top_words)
end = datetime.now()
print 'Top words were counted and saved in {diff} seconds'.format(diff=(end - start).seconds)
