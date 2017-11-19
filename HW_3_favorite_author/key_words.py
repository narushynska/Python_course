from summa import keywords

MIN_LETTERS = 5
# RATIO - percent of words
RATIO = 1.0


def get_top_words(text):
    temp = keywords.keywords(text, ratio=RATIO)
    res = ' '.join(word for word in temp.split() if len(word) >= MIN_LETTERS)
    return str(res)
