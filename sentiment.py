from pattern import en

def sentiment(text):
    sent = en.sentiment(text)
    return sent[0]

def min():
    return -1

def max():
    return 1
