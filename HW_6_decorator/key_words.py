from summa import keywords
from time import time

from utils import Logger

MIN_LETTERS = 5
# RATIO - percent of words
RATIO = 1.0
LOG_FILE = 'log.txt'

@Logger(LOG_FILE)
def get_top_words(text):
    start = time()
    temp = keywords.keywords(text, ratio=RATIO)
    res = ' '.join(word for word in temp.split() if len(word) >= MIN_LETTERS)
    end = time()
    print 'Top words were counted in {diff} seconds'.format(diff=(end - start))
    return str(res)
