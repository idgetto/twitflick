from pattern.web import Twitter

def fuzzy_find(thing):
    t = Twitter()

    fuzzy_things = fuzzy_list(thing)

    tweets = []
    for item in fuzzy_things:
        new_tweets = t.search(item, count=50, throttle=2)
        for tweet in new_tweets:
            ids = map(lambda x: x.id, tweets)
            if ids.count(tweet.id) == 0:
                tweets.append(tweet)

    return tweets

def fuzzy_list(thing):
    """ make a list of strings like thing
    >>> fuzzy_list('Harry Potter')
    ['Harry Potter', 'HARRY POTTER', 'harry potter', 'Harry potter', 'Harry Potter', 'HARRYPOTTER', 'harrypotter', 'Harrypotter']
    """

    things = []

    things.append(thing)
    things.append(thing.upper())
    things.append(thing.lower())
    things.append(thing.capitalize())
    things.append(thing.title())

    nospace = ''.join(thing.split())
    things.append(nospace.upper())
    things.append(nospace.lower())
    things.append(nospace.capitalize())

    return things

if __name__ == "__main__":
    import doctest
    doctest.testmod()
